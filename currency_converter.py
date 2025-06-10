def convert_currency(amount, from_currency, to_currency):
    # Function to convert an amount from one currency to another

    # Dictionary containing exchange rates for different currency pairs
    exchange_rates = {
        "USD": {"INR": 83.2, "EUR": 0.92},
        "INR": {"USD": 0.012, "EUR": 0.011},
        "EUR": {"USD": 1.09, "INR": 90.5},
    }

    # If the source and target currencies are the same, return the original amount
    if from_currency == to_currency:
        return amount
    
    try:
        # Retrieve the exchange rate for the specified currency pair
        rate = exchange_rates[from_currency][to_currency]
        # Calculate and return the converted amount
        return amount * rate
    
    except KeyError:
        # If the currency pair is not found in the exchange rates, return None
        return None
    

# Display available currencies to the user
print("Available Currencies: USD, INR, EUR")
from_currency = input("From Currency:").upper()  # Get the source currency from user input
to_currency = input("To Currency:").upper()  # Get the target currency from user input

try:
    amount = float(input("Amount to Convert:"))  # Get the amount to convert and convert it to float
    result = convert_currency(amount, from_currency, to_currency)  # Call the conversion function

    if result is not None:
        # If conversion is successful, display the result
        print(f"{amount} {from_currency} = {round(result, 2)} {to_currency} ")
    else:
        # If conversion is not supported, notify the user
        print("Conversion is not supported.")

except ValueError:
    # Handle the case where the input for amount is not a valid number
    print("Please enter a valid number for amount.")
