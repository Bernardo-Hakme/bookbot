#Contains all data_analysis functions

#Gets file content
def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

#Gets the number of words in a book
def word_count(book_content):
    num_words = book_content.split()
    return len(num_words)
