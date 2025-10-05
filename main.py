from stats import get_num_words, letter_counter
import sys

def get_book_text(file_path):
    with open(f"{file_path}") as f:
        read_file = f.read()
        return read_file
    
def main(path):
    num_words = len(get_num_words((get_book_text(path))))
    char_num = letter_counter(get_num_words(get_book_text(path)))
    char_num.sort()



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for letter, count in char_num:
        print(f"{letter}: {count}")

    print("============= END ===============")

if len(sys.argv) != 2:

    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

try:    
    path = sys.argv[1]
    main(path)
except:
    sys.exit(1)

