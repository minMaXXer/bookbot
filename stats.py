letter_dict = {}


def book_contents(contents):
    words = contents.split()
    content = 0
    for word in words:
        content += 1
    return content

def letter_count(contents):
    words = contents.split()
    letters =[char.lower() for word in words for char in word]
    for letter in letters:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort_letters(letters):
    items = list(letters.items())
    items.sort(key=lambda item: item[1], reverse = True)
    sorted = dict(items)
    return sorted
    
