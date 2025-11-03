def get_words_in_book(book):
    book_array = book.split()
    return len(book_array)

def count_characters(book):
    char_counts = dict()
    for char in book:
        char = char.lower()
        if(char in char_counts):
            char_counts[char] += 1
            continue
        char_counts[char] = 1
    return char_counts

def sort_dictionary(char_counts):
    dictlist = [dict()]
    for key in char_counts.keys():
        dictlist.append({"name": key, "num": char_counts[key]})
    dictlist.sort(reverse=True, key=sort_on)
    return dictlist

def sort_on(items):
    return items["num"]