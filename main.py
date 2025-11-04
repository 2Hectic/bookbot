import sys

from stats import get_words_in_book, count_characters, sort_dictionary

def get_book_Text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_Text(sys.argv[1])

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    num_words = get_words_in_book(book)
    char_details = count_characters(book)
    sorted_list = sort_dictionary(char_details)

    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        print(f"{item["name"]}: {item["num"]}")

main()