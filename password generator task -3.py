#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import secrets
import pyperclip

def generate_password(length, complexity):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    charset = ""
    if 'l' in complexity:
        charset += lowercase_letters
    if 'u' in complexity:
        charset += uppercase_letters
    if 'd' in complexity:
        charset += digits
    if 's' in complexity:
        charset += symbols

    if not charset:
        print("Invalid complexity! Please include at least one of 'l', 'u', 'd', 's'.")
        return None

    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password

def display_welcome():
    print("Welcome to Password Generator")

def display_farewell():
    print("Thank you for using Password Generator. Goodbye!")

def generate_passwords():
    while True:
        print("\nPASSWORD GENERATOR MENU:")
        print("1. Generate Password")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '2':
            display_farewell()
            break

        if choice == '1':
            length = input("Enter password length: ")
            complexity = input("Enter password complexity (l for lowercase, u for uppercase, d for digits, s for symbols, e.g., lud): ")

            try:
                length = int(length)
                if length <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid input! Please enter a positive integer for password length.")
                continue

            valid_complexity = set('ludse')
            if not set(complexity).issubset(valid_complexity):
                print("Invalid complexity! Please include only 'l', 'u', 'd', 's'.")
                continue

            password = generate_password(length, complexity)
            if password:
                print("Generated Password:", password)

                copy_to_clipboard = input("Do you want to copy the generated password to clipboard? (yes/no): ").lower()
                if copy_to_clipboard == 'yes':
                    pyperclip.copy(password)
                    print("Password copied to clipboard!")
        else:
            print("Invalid choice! Please choose again.")

def main():
    display_welcome()
    generate_passwords()

if __name__ == "__main__":
    main()


# In[ ]:




