# writing test for main.py
# # test.py
import unittest
from main import count_lines_words_chars
class TestWcTool(unittest.TestCase):
    def test_count_lines_words_chars(self):
        lines, words, chars = count_lines_words_chars("data/test.txt")
        self.assertEqual(lines, 7145)
        self.assertEqual(words, 58164)
        self.assertEqual(chars, 332147)
if __name__ == "__main__":
    unittest.main()
# Run the test
# $ python test.py
# 