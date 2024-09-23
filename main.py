def  main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    word_count = count_words(text)
    char_dict = sort_char(count_char(text))
    display_char_dict(path_to_file, word_count, char_dict)

def get_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_char(text):
    char = {}
    lowered = text.lower()
    for c in lowered:
        if 96 < ord(c) < 123:
            if c in char:
                char[c] += 1
            else:
                char[c] = 1
    return char

def sort_char(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1],
                       reverse=True))

def display_char_dict(path, word_count, char_dict):
    print(f"---Begin report of {path}")
    print(f"{word_count} words found in the document.")
    for char in char_dict:
        print(f"The {char} character was found {char_dict[char]} times")
    print("--- End report ---")
main()