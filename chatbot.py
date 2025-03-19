import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def chat_with_gpt():
    print("AI Chatbot is running! Type 'exit' to stop.")
    
    # Fetch API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found. Make sure it's set in the .env file.")
        return
    
    client = openai.OpenAI(api_key=api_key)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            bot_reply = response.choices[0].message.content
            print(f"Chatbot: {bot_reply}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_gpt()
