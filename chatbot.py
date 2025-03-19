from transformers import pipeline

# Load pre-trained chatbot model
chatbot = pipeline("text-generation", model="gpt2")

def chatbot_response(user_input):
    response = chatbot(
        user_input,
        max_length=50, 
        num_return_sequences=1,
        truncation = True, # explicitly exnable truncation
        pad_token_id = 50256 # avoid unnecessary padding warnings
        )
    return response[0]['generated_text']

# Simple test loop
if __name__ == "__main__":
    print("AI Chatbot is running! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))