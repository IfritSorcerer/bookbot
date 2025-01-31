def main():
    #The path used to read the file 
    book_path = "books/frankenstein.txt"

    #The following with block will read the text from the book_path variable and present a report
    with open(book_path) as f:
        file_contents = f.read()
    char_list=char_count(file_contents)

    print(f"--- Lets have a look at {book_path} ---")
    print(f"The total number of words present in the document is: {word_count(file_contents)}")
    for char in char_list:
        print(f"The '{char['char']}' character was found '{char['num']}' times")
    print(f"--- Thus concludes my book report ---")

#The word_count simply splits it and returns the number of words
def word_count(file_contents):
    word_count = file_contents.split()
    return len(word_count)    

#The char_count coverts the file to lowercase, then sorts the individual letters into a separate dictionary
def char_count(file_contents):
    char_dict = {}
    char_list = []
    cont_lowered = file_contents.lower()
    for char in cont_lowered:
        if char.isalpha() and char not in char_dict:
            char_dict[char] = 1
        elif char.isalpha():
            char_dict[char] += 1

    for key in char_dict:
        dict= {"char": key, "num": char_dict[key]}
        char_list.sort(key=sort_on, reverse=True)
        char_list.append(dict)
    return char_list
    
def sort_on(dict):
    return dict["num"]





main()