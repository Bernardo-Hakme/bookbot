from stats import get_book_text, word_count, char_count, char_sort

import sys

def main():
    frank_path = "/home/bernardo_hakme/workspace/GitHub/bookbot/books/frankenstein.txt"
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frank_path}")

    print("------------ Word Count ------------")
    frankenstein = get_book_text(frank_path)
    total_words = word_count(frankenstein)

    print(f"{total_words} words found in the document")
    
    print("------------ Char Count ------------")
    total_chars = char_count(frankenstein)
    
    sorted_total_chars = char_sort(total_chars)
    for i in sorted_total_chars:
        if i["char"].isalpha():    
            print(f"{i["char"]}: {i["num"]}")
    print("============ END ============")

    
main()