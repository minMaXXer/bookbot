import sys
from stats import book_contents, letter_count, sort_letters

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():

    book = get_book_text(sys.argv[1])
    words = book_contents(book)
    letters = letter_count(book)
    sorted = sort_letters(letters)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')
    print("----------- Word Count ----------")
    print(f'Found {words} total words')
    print("--------- Character Count -------")
    for letter in sorted:
        print(f'{letter}: {sorted[letter]}')
    print("============= END ===============")

if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()