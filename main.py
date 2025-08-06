from stats import get_book_text, word_count, char_count, char_sort

def main():
    frank_path = "/home/bernardo_hakme/workspace/GitHub/bookbot/books/frankenstein.txt"
    
    frankenstein = get_book_text(frank_path)
    total_words = word_count(frankenstein)

    print(f"{total_words} words found in the document")

    total_chars = char_count(frankenstein)
    
    sorted_total_chars = char_sort(total_chars)
    print(sorted_total_chars)

    
    
main()