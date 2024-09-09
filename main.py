def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()            #here we assign the entire text from the book to file_contents
        print(file_contents)
        words_count = 0                     # here we setup the word counting
        words = file_contents.split()
        for word in words:
            words_count += 1
        print(words_count)

if __name__ == "__main__":
    main()