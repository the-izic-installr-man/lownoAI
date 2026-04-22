# Main Chatbot Script for 1.6GB RAM Systems

# Import necessary libraries
from gpt4all import GPT

# Initialize GPT model
model = GPT(model='gpt4all', n_gpus=0)

# Function to handle chatbot mode
def chatbot_mode():
    print("Chatbot Mode Activated")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = model.generate(user_input)
        print(f"Chatbot: {response}")

# Function to handle coder mode
def coder_mode():
    print("Coder Mode Activated")
    while True:
        user_input = input("Code Request: ")
        if user_input.lower() == 'exit':
            break
        code_response = model.generate(user_input)
        print(f"Code: {code_response}")

# Main entry point
if __name__ == '__main__':
    mode = input("Choose mode (chatbot/coder): ").lower()
    if mode == 'chatbot':
        chatbot_mode()
    elif mode == 'coder':
        coder_mode()
    else:
        print("Invalid mode selected.")