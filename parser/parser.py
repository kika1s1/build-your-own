from typing import List
from lexer import Token, TokenType

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        
    def parse(self) -> bool:
        return self.parse_object()
    
    def parse_object(self) -> bool:
        # Check opening brace
        if self.pos >= len(self.tokens) or self.tokens[self.pos].type != TokenType.LEFT_BRACE:
            return False
            
        self.pos += 1  # Move past the opening brace
        
        # Handle empty object
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == TokenType.RIGHT_BRACE:
            self.pos += 1
            return True
            
        # Parse key-value pairs
        while self.pos < len(self.tokens):
            # Check for key (should be a string)
            if self.tokens[self.pos].type != TokenType.STRING:
                return False
            
            self.pos += 1
            
            # Check for colon after key
            if self.pos >= len(self.tokens) or self.tokens[self.pos].type != TokenType.COLON:
                return False
                
            self.pos += 1
            
            # Parse value (could be string, number, object, etc.)
            if not self.parse_value():
                return False
            
            # After a key-value pair, we expect either a comma or closing brace
            if self.pos >= len(self.tokens):
                return False
                
            if self.tokens[self.pos].type == TokenType.RIGHT_BRACE:
                self.pos += 1
                return True
                
            if self.tokens[self.pos].type != TokenType.COMMA:
                return False
                
            self.pos += 1  # Move past the comma
            
        return False  # If we get here, we never found the closing brace
        
    def parse_value(self) -> bool:
        if self.pos >= len(self.tokens):
            return False
            
        token = self.tokens[self.pos]
        
        # Handle different value types
        if token.type in [TokenType.STRING, TokenType.NUMBER, TokenType.TRUE, 
                         TokenType.FALSE, TokenType.NULL]:
            self.pos += 1
            return True
            
        # Handle nested objects
        if token.type == TokenType.LEFT_BRACE:
            return self.parse_object()
            
        # Handle arrays (to be implemented)
        if token.type == TokenType.LEFT_BRACKET:
            return self.parse_array()
            
        return False
        
    def parse_array(self) -> bool:
        # TODO: Implement array parsing
        return False 