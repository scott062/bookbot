def main():
    book_path = "books/frankenstein.txt"
    text = get_text_file(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    generate_report(book_path, word_count, char_count)

def get_word_count(str):
    return len(str.split())

def get_text_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_char_count(text):
    lowercase_text = text.lower()
    count = {}
    for char in lowercase_text:
        if count.get(char):
            count[char] += 1
        else:
            count[char] = 1
    return count


def generate_report(file_path, word_total, char_count):
    char_count_list = list(char_count.items())
    # Sort the list by the second tuple value aka the char count
    char_count_list.sort(reverse=True, key=lambda l: l[1])
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_total} words found in the document\n")
    for c in char_count_list:
        if c[0].isalpha():
            print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")


main()
