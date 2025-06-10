def show_menu():
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by Zero."
    return x / y

def modulo(x, y):
    if y == 0:
        return "Error! Modulo by Zero."
    return x % y

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "6":
        print("Goodbye! 👋")
        break  # Exit immediately without asking for numbers

    if choice in ["1", "2", "3", "4", "5"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", modulo(num1, num2))
    else:
        print("Invalid choice. Please select from 1 to 6.")
