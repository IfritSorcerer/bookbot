
def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents.lower()
        file_contents = f.read()

    print(f"Lets have a look at {book_path}")
    print(f"The total number of words present in the document is: {word_count(file_contents)}")


    print("Thus concludes my book report")

def word_count(file_contents):
    word_count = file_contents.split()
    return len(word_count)    






main()