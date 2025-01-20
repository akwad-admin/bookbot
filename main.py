# def main():
#     path = "books/frankenstein.txt"
#     lines = get_text(path)
#     words = get_words(lines)
#     result = get_characters(words)
#     print(result)
#     print(len(words))

# def get_text(path):
#     with open(path, 'r') as f:
#         lines = f.readlines()
#         return lines
    
# def get_words(lines):
#     words = []
#     for line in lines:
#         words.extend(line.split())
#     return words

# # def get_characters(words):
# #     # Convert all words to a single string, including spaces between words, and then to lowercase
# #     text = ' '.join(words).lower()
# #     char_count = {}
# #     for char in text:
# #         if char in char_count:
# #             char_count[char] += 1
# #         else:
# #             char_count[char] = 1
# #     return char_count


# def get_characters(words):
#     # Convert all words to a single string, including all types of whitespace, and then to lowercase
#     text = ' '.join(words).lower()
#     char_count = {}
#     for char in text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     char_count[' '] = text.count(' ')  # Count spaces explicitly
    

#     return char_count


# if __name__ == "__main__":
#     main()

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)

#     print("--- Begin report of books/frankenstein.txt ---")
#     print(f"{num_words} words found in the document\n")

#     for char, count in sorted_chars:
#         print(f"The '{char}' character was found {count} times")
    
#     print("--- End report ---")


#     print(chars_dict)


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
    



# main()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    # Sort characters by frequency in descending order
    sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)

    # Print only the top 26 characters (assuming we're dealing with English alphabet)
    for char, count in sorted_chars[:26]:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():  # Only count alphabetic characters
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()