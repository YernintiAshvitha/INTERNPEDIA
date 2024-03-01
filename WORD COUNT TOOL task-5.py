import string

def count_words(text):
    # Remove punctuation and split the text into words
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()

    # Count the number of words
    word_count = len(words)
    return word_count

def word_count_tool():
    while True:
        print("\nWORD COUNT TOOL MENU:")
        print("1. Count words from input text")
        print("2. Count words from a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '3':
            print("Exiting...")
            break

        if choice == '1':
            text = input("Enter the text: ")
            word_count = count_words(text)
            print("Word count:", word_count)

        elif choice == '2':
            file_name = input("Enter the file name: ")
            try:
                with open(file_name, 'r') as file:
                    text = file.read()
                    word_count = count_words(text)
                    print("Word count:", word_count)
            except FileNotFoundError:
                print("Error: File not found.")
            except IOError:
                print("Error: Unable to read the file.")
        
        else:
            print("Invalid choice! Please choose again.")

def main():
    print("Welcome to Word Count Tool")
    word_count_tool()

if __name__ == "__main__":
    main()
