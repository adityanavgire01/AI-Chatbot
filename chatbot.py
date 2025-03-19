def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
    }

    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand.")

# Simple test loop
if __name__ == "__main__":
    print("Chatbot is running! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))