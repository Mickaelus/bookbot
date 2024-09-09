def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)
    num_words = get_num_words(file_contents)
    print(f"{num_words} words found in the document")


def get_num_words(file_contents):   #gets the number of words in the book contents
    words = file_contents.split()
    return len(words)

def get_file_contents(file_path):   #gets the whole book contents
    with open(file_path) as f:
        return f.read()

if __name__ == "__main__":
    main()