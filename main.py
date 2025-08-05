def main():
    frank_path = "/home/bernardo_hakme/workspace/GitHub/bookbot/books/frankenstein.txt"
    frankenstein = get_book_text(frank_path)
    print(frankenstein)
    
def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()
    
    




main()