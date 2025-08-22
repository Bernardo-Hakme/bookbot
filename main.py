from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, "r") as file:
        file_data = file.read()
    return file_data

def main():
    text_frankenstein = get_book_text("books/frankenstein.txt")
    num_words = count_words(text_frankenstein)
    print(f"{num_words} words found in the document")
    num_chars = count_characters(text_frankenstein)
    print(num_chars)

main()