import unittest
from src.huffman import HuffmanTree

class TestHuffmanTree(unittest.TestCase):

    def setUp(self):
        self.huffman_tree = HuffmanTree()

    def test_build_tree(self):
        data = "hello huffman"
        self.huffman_tree.build_tree(data)
        self.assertIsNotNone(self.huffman_tree.root)

    def test_encode(self):
        data = "hello huffman"
        self.huffman_tree.build_tree(data)
        encoded_data = self.huffman_tree.encode(data)
        self.assertIsInstance(encoded_data, str)
        self.assertGreater(len(encoded_data), 0)

    def test_decode(self):
        data = "hello huffman"
        self.huffman_tree.build_tree(data)
        encoded_data = self.huffman_tree.encode(data)
        decoded_data = self.huffman_tree.decode(encoded_data)
        self.assertEqual(decoded_data, data)

if __name__ == '__main__':
    unittest.main()