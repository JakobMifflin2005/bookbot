from stats import split_words
from stats import count_letters

#opens book from file
def get_book_text(filepath): 
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#splits words in book
def split_words(book):
    words = book.split()
    return len(words)



def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = split_words(book)
    print(f"{word_count} words found in the document")
    print(count_letters(book))
main()