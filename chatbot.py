print("🤖 Chatbot: Hello! I am your simple rule-based chatbot.")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "exit":
        print("🤖 Chatbot: Goodbye! Have a great day 😊")
        break

    # Responses
    if "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hi there! How can I help you?")
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")
    elif "name" in user_input:
        print("🤖 Chatbot: I'm a chatbot created by you!")
    elif "time" in user_input:
        print("🤖 Chatbot: I can't tell time yet, but maybe in the future ⏳")
    elif "weather" in user_input:
        print("🤖 Chatbot: I don't know the weather, but I hope it's sunny ☀️")
    elif "bye" in user_input:
        print("🤖 Chatbot: Bye! Talk to you soon 👋")
        break
    else:
        print("🤖 Chatbot: Sorry, I don't understand that. Try asking something else.")
