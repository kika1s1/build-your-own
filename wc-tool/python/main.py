# building my own wc tool
# wc-tool is a command line tool that counts the number of lines, words, and characters in a file.
# answer
import sys
def count_lines_words_chars(filename):
    with open(filename, 'r',  encoding='utf-8') as file:
        text = file.read()
        lines = text.splitlines()
        words = text.split()
        num_lines = len(lines)
        num_words = len(words)
        num_chars = len(text)
        return num_lines, num_words, num_chars

if __name__ == "__main__":
    if sys.argv[-1] == "-h":
        print("Usage: python main.py <filename>")
        sys.exit(1)
    filename = sys.argv[-1]
    try:
        lines, words, chars = count_lines_words_chars(filename)
        if sys.argv[1] == '-c':
                print(f" {chars} {filename}")
        elif sys.argv[1] == '-l':
            print(f" {lines} {filename}")
        elif sys.argv[1] == '-w':
            print(f" {words} {filename}")
        else:
            print(f" {lines} {words} {chars} {filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)
        