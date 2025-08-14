import sys
from stats import split_words
from stats import count_letters
from stats import sort_dict\


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

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
    book_title = sys.argv[1]
    book = get_book_text(sys.argv[1])
    book_counts = count_letters(book)
    word_count = split_words(book)
    letter_count = count_letters(book)
    sorted_list = sort_dict(letter_count)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_title}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()