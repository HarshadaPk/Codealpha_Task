# 📌 Basic Rule-Based Chatbot
# Key Concepts: if-elif, functions, loops, input

def chatbot():
    print(" Chatbot: Hello! I'm your chatbot. Type 'bye' to exit.")

    while True:  # Loop to keep chatbot running
        user_input = input("You: ").lower()  # Take user input

        # Rule-based responses using if-elif
        if user_input == "hi" or user_input == "hello":
            print(" Chatbot: Hello! How can I help you?")
        
        elif user_input == "how are you":
            print(" Chatbot: I'm fine")
        
        elif user_input == "good morning":
            print(" Chatbot: Good morning! Have a great day ahead.")
        
        elif user_input == "what is your name":
            print(" Chatbot: I'm a simple chatbot made in Python.")
        
        elif user_input == "bye":
            print(" Chatbot: Goodbye!")
            break  # Exit loop
        
        else:
            print(" Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
