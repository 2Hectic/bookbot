from stats import get_words_in_book, count_characters, sort_dictionary

def get_book_Text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    print
    book = get_book_Text("./books/frankenstein.txt")
    num_words = get_words_in_book(book)
    char_details = count_characters(book)
    sorted_list = sort_dictionary(char_details)
    print(f"Found {num_words} total words")
    print(char_details)

main()