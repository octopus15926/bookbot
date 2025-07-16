def get_num_words(book_text: str) -> int:
    num_words = len(book_text.split())
    return num_words

def get_num_characters_as_dict(book_text: str) -> dict:
    lower_book_text = book_text.lower()
    char_dictionary = {}
    for char in lower_book_text:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def get_sorted_list(char_dict) -> list:
    dict_list = []
    for char in char_dict:
        temp_char_dict = {
            "char": char,
            "num": char_dict[char]
            }
        dict_list.append(temp_char_dict)
    dict_list.sort(reverse=True, key=get_key_to_sort)
    return dict_list

def get_key_to_sort(char_dict) -> int:
    return char_dict["num"]