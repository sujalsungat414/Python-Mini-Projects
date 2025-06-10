import time  # Import the time module to use sleep function

def countdown(seconds):
    # Function to perform a countdown from a given number of seconds
    while seconds > 0:  # Continue until the countdown reaches zero
        mins, secs = divmod(seconds, 60)  # Calculate minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format the time as MM:SS
        print(timer, end="\r")  # Print the timer on the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1  # Decrease the seconds by 1

    print("Time's up! ⏰")  # Notify when the countdown is complete

try:
    total_seconds = int(input("Enter time in seconds:"))  # Get user input and convert to integer
    countdown(total_seconds)  # Call the countdown function with the user input

except ValueError:
    print("Please enter a valid number.")  # Handle invalid input
