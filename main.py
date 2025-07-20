from stats import get_num_words
from stats import get_book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
 #   split_text = raw_text.split()
    print(f"{get_num_words(book_text)} words found in the document")
    return None

main()