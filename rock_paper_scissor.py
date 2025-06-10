import random  # Import the random module to allow random selection

# List of valid choices for the game
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")  # Welcome message for the user

while True:  # Start an infinite loop to allow multiple rounds of the game
    user_choice = input("Enter your choice (rock, paper, scissors): ")  # Prompt user for their choice

    if user_choice not in choices:  # Check if the user's choice is valid
        print("Invalid choice. Try again.")  # Inform the user of the invalid choice
        continue  # Restart the loop to allow for a new input

    computer_choice = random.choice(choices)  # Randomly select the computer's choice
    print(f"Computer chose: {computer_choice}")  # Display the computer's choice

    # Check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")

    # Check for a win condition for the user
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")  # Inform the user they have won

    else:
        print("😓 You lose!")  # Inform the user they have lost

    # Ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()  # Convert input to lowercase for consistency
    if play_again != "yes":  # If the user does not want to play again
        print("Thanks for playing!")  # Thank the user for playing
        break  # Exit the loop and end the game
