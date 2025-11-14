import sys
from stats import word_count, char_count, print_report

def get_book_text(filepath):
    # The with block will automatically close the file when the block is exited, cleaning up resources.
    with open(filepath) as f:
            # do something with f (the file) here
            # f is a file object
        file_contents = f.read()
    return file_contents

 
def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        my_path = sys.argv[1]
        print(my_path)
        book_content = get_book_text(my_path)
        count = word_count(book_content)
        char_dict = char_count(book_content)
        print_report(count, char_dict)
    except Exception as e:
        print(e)
        return e


main()