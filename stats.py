def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count

def sort_on(list):
    return list["num"]


def sorted_dict(count):
    slist = []
    for key, value in count.items():
        temp_dict = {
            "char": key,
            "num": value
        }
        slist.append(temp_dict)
    slist.sort(reverse=True, key=sort_on)
    return slist