import random  # Import the random module to generate random numbers

def roll_dice():
    # Returns a random integer between 1 and 6 inclusive, simulating a dice roll
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Roller Simulator!")  # Welcome message

while True:  # Infinite loop to allow multiple dice rolls
    input("Press Enter to roll the dice...")  # Prompt user to roll the dice
    result = roll_dice()  # Call the roll_dice function to get a random roll result
    print(f"You rolled a {result} 🥳")  # Display the result of the dice roll

    choice = input("Do you want to roll again? (y/n):").lower()  # Ask if the user wants to roll again

    if choice != "y":  # If the user does not enter 'y', exit the loop
        print("Thanks for playing! GoodBye 🙋‍♂️")  # Goodbye message
        break  # Exit the loop and end the program
