def main():
    book_file_path = "books/frankenstein.txt"
    text = get_text(book_file_path)

    word_count = get_word_count(text)
    print(f"This book contains {word_count} words!")

    print(get_char_dict(text))

def get_text(book_file_path):
    with open(book_file_path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()