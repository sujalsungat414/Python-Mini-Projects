def counter_app():
    count = 0  # Initialize the counter variable to zero

    while True:  # Start an infinite loop to keep the app running
        print(f"Current count: {count}")  # Display the current count
        print("Press 1 for Increment\nPress 2 for Decrement\nPress 3 for Reset \nPress 4 for Quit")  # Show options to the user
        choice = int(input())  # Get user input and convert it to an integer

        if choice == 1:  # If the user chooses to increment
            count += 1  # Increase the count by 1
        
        elif choice == 2:  # If the user chooses to decrement
            count -= 1  # Decrease the count by 1

        elif choice == 3:  # If the user chooses to reset
            count = 0  # Reset the count to zero

        elif choice == 4:  # If the user chooses to quit
            print("Thanks!")  # Thank the user for using the app
            break  # Exit the loop and end the program

        else:  # If the user enters an invalid option
            print("Choose valid input")  # Prompt the user to choose a valid input
        
print("Welcome To Counter-App\n")  # Welcome message for the user
counter_app()  # Call the counter_app function to start the application
