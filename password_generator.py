import random  # Import the random module to generate random choices
import string  # Import the string module to access predefined character sets

def password_generator(length):
    # Function to generate a random password of a specified length
    # Combine uppercase, lowercase letters, digits, and punctuation characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the combined set
    password = "".join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password


try:
    length = int(input("Enter password length: "))  # Prompt user for the desired password length and convert to integer
    if length < 6:  # Check if the length is less than the minimum requirement
        print("Password should be at least 6 characters long.")  # Inform the user of the minimum length requirement
    
    else:
        password = password_generator(length)  # Call the password_generator function to create a password
        print("Generated Password:", password)  # Display the generated password

except ValueError:  # Handle the case where the input is not a valid integer
    print("Please enter a valid number.")  # Prompt the user to enter a valid number
