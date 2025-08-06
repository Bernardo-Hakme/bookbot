import stats

def main():
    frank_path = "/home/bernardo_hakme/workspace/GitHub/bookbot/books/frankenstein.txt"
    
    frankenstein = stats.get_book_text(frank_path)
    total_words = stats.word_count(frankenstein)

    print(f"{total_words} words found in the document")

    total_chars = stats.char_count(frankenstein)
    print(total_chars)
main()