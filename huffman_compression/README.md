# Huffman Compression Tool

This project implements a compression tool using the Huffman encoding algorithm. Huffman coding is a widely used method of lossless data compression that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

## Project Structure

```
huffman_compression/
├── src/
│   ├── huffman.py       # Implementation of the Huffman encoding algorithm
│   └── utils.py         # Utility functions for frequency calculation and file handling
├── tests/
│   └── test_huffman.py  # Unit tests for the Huffman encoding implementation
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies
```

## Installation

To get started with the Huffman compression tool, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd huffman_compression
pip install -r requirements.txt
```

## Usage

To use the Huffman compression tool, you can import the `HuffmanTree` class from the `huffman.py` file and utilize its methods to encode and decode data. Here’s a simple example:

```python
from src.huffman import HuffmanTree

# Sample data
data = "this is an example for huffman encoding"

# Create a Huffman tree
huffman_tree = HuffmanTree()
huffman_tree.build_tree(data)

# Encode the data
encoded_data = huffman_tree.encode(data)
print(f"Encoded Data: {encoded_data}")

# Decode the data
decoded_data = huffman_tree.decode(encoded_data)
print(f"Decoded Data: {decoded_data}")
```

## Running Tests

To ensure the correctness of the implementation, run the unit tests located in the `tests` directory:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.