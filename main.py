def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_path)
    num_words = get_num_words(file_contents)
    num_characters = get_num_characters(file_contents)
    sorted_characters = sorted(num_characters.items(), key=lambda x: x[1], reverse=True) #gets the number of character listed sorted in order of frequency
    print(f"\n--- Begin report of {file_path} ---") #this is a header, to make the separation between the word count and the character count easier to see
    print(f"{num_words} words found in the document")
    for character, count in sorted_characters: 
            print(f"The '{character}' character was found {count} times")
    print("\n--- End report ---")

def get_num_words(file_contents):   #gets the number of words in the book contents
    words = file_contents.split()
    return len(words)

def get_file_contents(file_path):   #gets the whole book contents
    with open(file_path) as f:
        return f.read()

def get_num_characters(file_contents): #gets a count of each character
    characters = {}
    for character in file_contents.lower():
        if character.isalpha(): #checks if the character is a letter, used to sort out specific characters such as ? or !
            characters[character] = characters.get(character, 0) + 1 #adds the character to the dictionary if it doesn't already exist, or add one to the count if it does
    return characters

if __name__ == "__main__":
    main()