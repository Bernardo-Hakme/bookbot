from stats import count_words, count_characters, sorted_characters

import sys

def get_book_text(filepath):
    with open(filepath, "r") as file:
        file_data = file.read()
    return file_data

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text_book = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    print("----------- Word Count ----------")
    num_words = count_words(text_book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = count_characters(text_book)
    pre_report = sorted_characters(num_chars)
    for d in pre_report:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()