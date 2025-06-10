import random  # Import the random module to generate random numbers

def number_guessing_game():
    # Function to run the number guessing game
    print("🎯 Welcome to the Number Guessing Game!")  # Welcome message
    print("I'm thinking of a number between 1 and 100.")  # Instructions for the player

    secret_number = random.randint(1, 100)  # Generate a random secret number between 1 and 100
    attempts = 0  # Initialize the number of attempts to zero

    while True:  # Start an infinite loop to allow multiple guesses
        try:
            guess = int(input("Enter your guess:"))  # Prompt the user for their guess and convert it to an integer
            attempts += 1  # Increment the attempt counter

            if guess < secret_number:  # If the guess is lower than the secret number
                print("Too low! Try again.\n")  # Inform the user that their guess is too low

            elif guess > secret_number:  # If the guess is higher than the secret number
                print("Too high! Try again.\n")  # Inform the user that their guess is too high

            else:  # If the guess is correct
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")  # Congratulate the user and show the number of attempts
                break  # Exit the loop

        except ValueError:  # Handle the case where the input is not a valid integer
            print("❌ Please enter a valid number.")  # Prompt the user to enter a valid number

number_guessing_game()  # Call the function to start the game
