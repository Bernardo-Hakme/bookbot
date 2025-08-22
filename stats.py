def count_words(text):
    return len(text.split())

def count_characters(text):
    lower_text = text.lower()
    chars_dict = {}
    for c in lower_text:
        if c not in chars_dict:
            chars_dict[c] = 1
        else:
            chars_dict[c] += 1
    return chars_dict