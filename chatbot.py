from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a pre-trained chat model (DialoGPT)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chatbot_response(user_input):
    # Encode input text and generate a response
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Generate a response with controlled randomness
    output_ids = model.generate(
        input_ids,
        max_length=100,
        temperature=0.7,  # Lower temperature for more focused responses
        top_k=50,  # Avoids random outputs
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Simple test loop
if __name__ == "__main__":
    print("AI Chatbot is running! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))
