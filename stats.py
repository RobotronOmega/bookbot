def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())