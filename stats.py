def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def get_num_words():
    book_text = get_book_text()
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")