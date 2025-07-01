#splits words in book
def split_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = {}
    for x in book:
        char = x.lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
