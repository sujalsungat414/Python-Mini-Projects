print("Welcome to the Tip Calculator!")  # Welcome message for the user

bill = float(input("What was the total bill? ₹ "))  # Prompt user for total bill amount, convert input to float

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))  # Ask for tip percentage, convert to int

people = int(input("How many people to split the bill? "))  # Ask for number of people splitting the bill, convert to int

tip = bill * (tip_percentage / 100)  # Calculate the tip amount based on the bill and tip percentage

total_bill = bill + tip  # Calculate the total bill including tip

amount_per_person = total_bill / people  # Divide total bill by number of people to find amount per person

final_amount = round(amount_per_person, 2)  # Round the amount per person to 2 decimal places

print(f"Each person should pay: ₹{final_amount}")  # Display the final amount each person should pay
