#splits words in book
def split_words(book):
    words = book.split()
    return len(words)


#counts lettersS
def count_letters(book):
    letters = {}
    for x in book:
        char = x.lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters



def sort_on(items):
    return items["num"]



def sort_dict(book):
    sorted_list = []
    for ch in book:
        sorted_list.append({"char": ch, "num": book[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

