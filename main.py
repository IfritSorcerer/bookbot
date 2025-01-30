def main():
    #The path used to read the file 
    book_path = "books/frankenstein.txt"

    #The following with block will read the text from the book_path variable
    with open(book_path) as f:
        file_contents = f.read()

    print(f"--- Lets have a look at {book_path} ---")
    print(f"The total number of words present in the document is: {word_count(file_contents)}")

    print(f"{char_count(file_contents)}")
    print(f"--- Thus concludes my book report ---")


def word_count(file_contents):
    word_count = file_contents.split()
    return len(word_count)    

def char_count(file_contents):
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    





main()