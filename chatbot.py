def chatbot():
    print("Chatbot: Hi! Type something (type 'bye' to exit)")

    while True:
        try:
            user_input = input("You: ").strip().lower()
        except EOFError:
            print("\nChatbot: Goodbye!")
            break

        if user_input == "":
            print(user_input)
            print("Chatbot: Please say something.")
        
        elif user_input == "hello":
            print(user_input)
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print(user_input)
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print(user_input)
            print("Chatbot: Goodbye!")
            break

        else:
            print(user_input)
            print("Chatbot: Sorry, I don't understand.")

chatbot()