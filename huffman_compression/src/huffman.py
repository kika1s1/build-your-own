class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, data):
        frequency = self.get_frequency(data)
        priority_queue = [Node(char, freq) for char, freq in frequency.items()]
        priority_queue.sort(key=lambda x: x.freq)

        while len(priority_queue) > 1:
            left = priority_queue.pop(0)
            right = priority_queue.pop(0)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            priority_queue.append(merged)
            priority_queue.sort(key=lambda x: x.freq)

        self.root = priority_queue[0]
        self.generate_codes(self.root, "")

    def get_frequency(self, data):
        frequency = {}
        for char in data:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def generate_codes(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
        self.generate_codes(node.left, current_code + "0")
        self.generate_codes(node.right, current_code + "1")

    def encode(self, data):
        encoded_output = ""
        for char in data:
            encoded_output += self.codes[char]
        return encoded_output

    def decode(self, encoded_data):
        decoded_output = ""
        current_node = self.root
        for bit in encoded_data:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_output += current_node.char
                current_node = self.root
        return decoded_output