import sys
from stats import get_num_words, get_num_characters_as_dict, get_sorted_list


def get_book_text(filepath) -> str:
    with open(filepath) as b:
        book = b.read()
        return book


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    char_dict = get_num_characters_as_dict(book)
    sorted_dicts = get_sorted_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for sd in sorted_dicts:
        if sd["char"].isalpha():
            print(f"{sd["char"]}: {sd["num"]}")


if __name__ == "__main__":
    main()
