def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)
    num_words = get_num_words(file_contents)
    num_characters = get_num_characters(file_contents)
    print(f"{num_words} words found in the document")
    print("\n--- Character Counts ---") #this is a header, to make the separation between the word count and the character count easier to see
    for character, count in sorted(num_characters.items()): #gets the number of character listed sorted in alphabetical order
        if character.isalpha(): #checks if the character is a letter, used to sort out specific characters such as ? or !
            print(f"The '{character}' character was found {count} times")

def get_num_words(file_contents):   #gets the number of words in the book contents
    words = file_contents.split()
    return len(words)

def get_file_contents(file_path):   #gets the whole book contents
    with open(file_path) as f:
        return f.read()

def get_num_characters(file_contents): #gets a count of each character
    lowered_file_contents = file_contents.lower()
    characters = {}
    for character in lowered_file_contents:
        characters[character] = characters.get(character, 0) + 1
    return characters

if __name__ == "__main__":
    main()