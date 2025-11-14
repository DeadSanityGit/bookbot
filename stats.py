def word_count(book_content):
    list_of_words = book_content.split()
    return len(list_of_words)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["count"]

def char_count(book_content):
    
    char_dict = {}
    list_from_dict = [{"char":"", "count":0}]

    words = book_content.split()
    for word in words:
        split_word = list(word)
        for char in split_word:
            tested_char = char.lower()
            if(tested_char in char_dict):
                char_dict[tested_char] += 1
            else:
                char_dict[tested_char] = 1
        char_dict.pop("", "Key not found")

    for key in char_dict.keys():
        list_from_dict.append({"char":key, "count":char_dict[key]})
    
    list_from_dict.sort(reverse=True,key=sort_on)
    return list_from_dict


def print_report(word_count, items):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in items:
        bla = item["char"]
        if bla.isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")