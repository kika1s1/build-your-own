from enum import Enum
from dataclasses import dataclass
from typing import List

class TokenType(Enum):
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    WHITESPACE = "WHITESPACE"
    ERROR = "ERROR"
    STRING = "STRING"
    COLON = ":"
    COMMA = ","
    NUMBER = "NUMBER"
    TRUE = "TRUE"
    FALSE = "FALSE"
    NULL = "NULL"
    ARRAY = "ARRAY"
    OBJECT = "OBJECT"
    KEY = "KEY"
    END_OF_FILE = "END_OF_FILE"

@dataclass
class Token:
    type: TokenType
    value: str
    position: int

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.text):
            current_char = self.text[self.pos]
            
            if current_char.isspace():
                self.pos += 1
                continue
                
            if current_char == '{':
                self.tokens.append(Token(TokenType.LEFT_BRACE, '{', self.pos))
                self.pos += 1
                continue
                
            if current_char == '}':
                self.tokens.append(Token(TokenType.RIGHT_BRACE, '}', self.pos))
                self.pos += 1
                continue
                
            if current_char == '[':
                self.tokens.append(Token(TokenType.LEFT_BRACKET, '[', self.pos))
                self.pos += 1
                continue
                
            if current_char == ']':
                self.tokens.append(Token(TokenType.RIGHT_BRACKET, ']', self.pos))
                self.pos += 1
                continue
                
            if current_char == ':':
                self.tokens.append(Token(TokenType.COLON, ':', self.pos))
                self.pos += 1
                continue
                
            if current_char == ',':
                self.tokens.append(Token(TokenType.COMMA, ',', self.pos))
                self.pos += 1
                continue
                
            if current_char == '"':
                string_token = self.tokenize_string()
                if string_token:
                    self.tokens.append(string_token)
                continue
                
            if current_char.isdigit() or current_char == '-':
                number_token = self.tokenize_number()
                if number_token:
                    self.tokens.append(number_token)
                continue
                
            if current_char.isalpha():
                word_token = self.tokenize_keyword()
                if word_token:
                    self.tokens.append(word_token)
                continue
                
            # If we get here, we've encountered an invalid character
            self.tokens.append(Token(TokenType.ERROR, current_char, self.pos))
            self.pos += 1
            
        return self.tokens
        
    def tokenize_string(self) -> Token | None:
        start_pos = self.pos
        self.pos += 1  # Skip opening quote
        value = ""
        
        while self.pos < len(self.text):
            current_char = self.text[self.pos]
            
            if current_char == '"':
                self.pos += 1  # Skip closing quote
                return Token(TokenType.STRING, value, start_pos)
                
            if current_char == '\\':
                self.pos += 1
                if self.pos >= len(self.text):
                    return Token(TokenType.ERROR, value, start_pos)
                value += self.text[self.pos]
            else:
                value += current_char
                
            self.pos += 1
            
        return Token(TokenType.ERROR, value, start_pos)
        
    def tokenize_number(self) -> Token | None:
        start_pos = self.pos
        value = ""
        
        # Handle negative numbers
        if self.text[self.pos] == '-':
            value += '-'
            self.pos += 1
            
        while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
            value += self.text[self.pos]
            self.pos += 1
            
        return Token(TokenType.NUMBER, value, start_pos)
        
    def tokenize_keyword(self) -> Token | None:
        start_pos = self.pos
        value = ""
        
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            value += self.text[self.pos]
            self.pos += 1
            
        if value == "true":
            return Token(TokenType.TRUE, value, start_pos)
        elif value == "false":
            return Token(TokenType.FALSE, value, start_pos)
        elif value == "null":
            return Token(TokenType.NULL, value, start_pos)
        else:
            return Token(TokenType.ERROR, value, start_pos) 