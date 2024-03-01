


# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

# Function to display welcome message
def display_welcome():
    print("Welcome to Simple Calculator")

# Function to display farewell message
def display_farewell():
    print("Thank you for using Simple Calculator. Goodbye!")

# Function to handle user input and perform calculations
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            display_farewell()
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print("Result:", result)
        else:
            print("Invalid input. Please enter a valid number.")

# Main function to start the program
def main():
    display_welcome()
    calculator()

if __name__ == "__main__":
    main()




