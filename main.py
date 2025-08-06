def main():
    frank_path = "/home/bernardo_hakme/workspace/GitHub/bookbot/books/frankenstein.txt"
    frankenstein = get_book_text(frank_path)
    total_words = word_count(frankenstein)
    print(f"{total_words} words found in the document")

#Gets file content
def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

#Gets the number of words in a book
def word_count(book_content):
    num_words = book_content.split()
    return len(num_words)

    




main()