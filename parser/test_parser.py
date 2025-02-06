import unittest
from lexer import Lexer
from parser import Parser

class TestJSONParser(unittest.TestCase):
    def assert_json_valid(self, json_str: str):
        lexer = Lexer(json_str)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        self.assertTrue(parser.parse(), f"JSON should be valid: {json_str}")
        
    def assert_json_invalid(self, json_str: str):
        lexer = Lexer(json_str)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        self.assertFalse(parser.parse(), f"JSON should be invalid: {json_str}")
    
    def test_empty_object(self):
        # Test valid empty object
        self.assert_json_valid("{}")
        
    def test_simple_key_value(self):
        # Test simple key-value pairs with different value types
        valid_cases = [
            '{"key": "value"}',
            '{"key": 123}',
            '{"key": true}',
            '{"key": false}',
            '{"key": null}'
        ]
        for case in valid_cases:
            self.assert_json_valid(case)
        
    def test_multiple_key_values(self):
        json = '''
        {
            "name": "Sample Project",
            "key": "value",
            "key2": "value2",
            "number": 123,
            "boolean": true,
            "null_value": null
        }
        '''
        self.assert_json_valid(json)
        
    def test_nested_object(self):
        json = '''
        {
            "name": "Sample Project",
            "nested": {
                "key1": "value1",
                "key2": "value2",
                "deep_nested": {
                    "key3": "value3"
                }
            }
        }
        '''
        self.assert_json_valid(json)
        
    def test_invalid_json(self):
        invalid_cases = [
            "",                     # Empty string
            "{",                    # Unclosed brace
            "}",                    # Only closing brace
            "abc",                  # Random text
            '{"key": }',           # Missing value
            '{"key" "value"}',     # Missing colon
            '{"key": "value",}',   # Trailing comma
            '{key: "value"}',      # Unquoted key
            '{"key": "value"',     # Unclosed object
            '{"a": {"b": "c",}}',  # Nested object with trailing comma
            '{"a": undefined}',    # Invalid value type
            '{"a": \'string\'}',   # Single quotes not allowed
            '{"a": 123.}',         # Invalid number format
            '{123: "value"}'       # Non-string key
        ]
        
        for case in invalid_cases:
            self.assert_json_invalid(case)
            
    def test_whitespace(self):
        # Test various whitespace scenarios
        valid_cases = [
            '{"key":"value"}',      # No spaces
            '{ "key" : "value" }',  # Extra spaces
            '''
            {
                "key": "value"
            }
            '''                     # Multiple lines and indentation
        ]
        for case in valid_cases:
            self.assert_json_valid(case)

if __name__ == '__main__':
    unittest.main() 