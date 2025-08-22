from stats import count_words, count_characters, sorted_characters

def get_book_text(filepath):
    with open(filepath, "r") as file:
        file_data = file.read()
    return file_data

def main():
    text_frankenstein = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    num_words = count_words(text_frankenstein)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = count_characters(text_frankenstein)
    pre_report = sorted_characters(num_chars)
    for d in pre_report:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()