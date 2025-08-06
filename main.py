from stats import get_book_text, word_count, char_count, char_sort

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path/to/file>")
        sys.exit(1)   

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")

    print("------------ Word Count ------------")
    book = get_book_text(sys.argv[1])
    total_words = word_count(book)

    print(f"{total_words} words found in the document")
    
    print("------------ Char Count ------------")
    total_chars = char_count(book)
    
    sorted_total_chars = char_sort(total_chars)
    for i in sorted_total_chars:
        if i["char"].isalpha():    
            print(f"{i["char"]}: {i["num"]}")
    print("============ END ============")

    
main()