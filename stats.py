#Contains all data_analysis functions

#Gets file content
def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

#Gets the number of words in a book
def word_count(book_content):
    num_words = book_content.split()
    return len(num_words)

#Getting the number each char appears in a text
def char_count(book_content):
    lower_text = book_content.lower()
    alpunct = {}
    used_chars = "abcdefghijklmopqrstuvwxyz.!?, /-()&%$#"
    
    for i in lower_text:
        for j in used_chars:
            if i == j:
                alpunct[i] = 0
    
    for i in lower_text:
        for j in used_chars:
            if i == j:
                alpunct[i] += 1
    return alpunct

#Creates a list of dictionaries and sort it based on the number of chars
def char_sort(dict_chars):
    dict_list = []
    for k, v in dict_chars.items():
        dict_list.append({"char": k, "num": v})
    
    dict_list.sort(reverse=True, key=lambda items: items["num"])
    return dict_list