import sys
from stats import get_num_words
from stats import get_book_text
from stats import count_characters
from stats import sorted_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
#   Get text from book    
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    count = count_characters(book_text)
    sdict = sorted_dict(count)
    for i in range(len(sdict)):
        if sdict[i]["char"].isalpha():
            print(f"{sdict[i]["char"]}: {sdict[i]["num"]}")
    print("============= END ===============")
    return None

main()