import argparse
import json
from huffman import HuffmanTree, Node

def main():
    parser = argparse.ArgumentParser(description="Huffman compression tool")
    parser.add_argument("input_file", help="Input file to compress or decompress")
    parser.add_argument("output_file", help="Output file")
    parser.add_argument("mode", choices=["compress", "decompress"], help="Mode of operation")
    args = parser.parse_args()

    if args.mode == "compress":
        with open(args.input_file, "r") as f:
            data = f.read()
        tree = HuffmanTree()
        tree.build_tree(data)
        encoded_data = tree.encode(data)

        # Store the frequency table as a header in the output file
        frequency = tree.get_frequency(data)
        header = json.dumps(frequency)  # Serialize the frequency table to JSON

        # Combine the header and encoded data
        output_data = header + "\n" + encoded_data

        # Writing the combined data to the output file
        with open(args.output_file, "w") as f:
            f.write(output_data)
        print(f"Compressed data written to {args.output_file}")

    elif args.mode == "decompress":
        with open(args.input_file, "r") as f:
            content = f.read()

        # Split the content into header and encoded data
        header, encoded_data = content.split("\n", 1)

        # Deserialize the frequency table from the header
        frequency = json.loads(header)  # Deserialize the JSON to a dictionary

        # Rebuild the Huffman tree from the frequency table
        # This time, we'll rebuild the tree using the frequency table directly
        priority_queue = [Node(char, freq) for char, freq in frequency.items()]
        priority_queue.sort(key=lambda x: x.freq)

        tree = HuffmanTree()  # Create a new HuffmanTree instance

        while len(priority_queue) > 1:
            left = priority_queue.pop(0)
            right = priority_queue.pop(0)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            priority_queue.append(merged)
            priority_queue.sort(key=lambda x: x.freq)

        tree.root = priority_queue[0]
        tree.generate_codes(tree.root, "")

        decoded_data = tree.decode(encoded_data)

        # Writing the decoded data to the output file
        with open(args.output_file, "w") as f:
            f.write(decoded_data)
        print(f"Decompressed data written to {args.output_file}")

if __name__ == "__main__":
    main()