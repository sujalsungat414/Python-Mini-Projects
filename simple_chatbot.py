print("🤖 Hello! I'm a simple chatbot. Type 'bye' to exit.")  # Welcome message for the user

# Infinite loop for chatting
while True:
    user_input = input("You: ").lower()  # Get user input and convert it to lowercase for easier matching

    # Check if the user greets the bot
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")  # Respond to greetings

    # Check if the user asks how the bot is doing
    elif "how are you" in user_input:
        print("Bot: I'm just a bunch of code, but I'm doing fine! 😊")  # Respond to inquiries about the bot's well-being

    # Check if the user asks for the bot's name
    elif "name" in user_input:
        print("Bot: I'm ChatBot 1.0!")  # Provide the bot's name

    # Check if the user wants to exit the chat
    elif "bye" in user_input:
        print("Bot: Goodbye! 👋")  # Farewell message
        break  # Exit the loop and end the chat

    # Handle any other input that doesn't match the above conditions
    else:
        print("Bot: Sorry, I didn't understand that.")  # Inform the user that the input was not understood
