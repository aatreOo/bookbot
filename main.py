import sys
print(sys.argv)
from stats import get_char_counts, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    with open(path) as f:
        book_text = f.read()
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()