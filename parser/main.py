import sys
from lexer import Lexer, TokenType
from parser import Parser

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <json_file>")
        sys.exit(1)
        
    try:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
            
        # Lexical analysis
        lexer = Lexer(content)
        tokens = lexer.tokenize()
        # print(tokens)
        
        # Check for lexical errors
        if any(token.type == TokenType.ERROR for token in tokens):
            print("Invalid JSON")
            sys.exit(1)
            
        # Parsing
        parser = Parser(tokens)
        is_valid = parser.parse()
        
        if is_valid:
            print("Valid JSON")
            sys.exit(0)
        else:
            print("Invalid JSON")
            sys.exit(1)
            
    except FileNotFoundError:
        print(f"Error: Could not open file {sys.argv[1]}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 