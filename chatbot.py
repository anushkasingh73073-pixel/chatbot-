# Simple Chatbot

print("=== Simple Chatbot ===")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower().strip()

    # Greeting
    if user == "hello" or user == "hi":
        print("Bot: Hello!")

    # Bot name
    elif "name" in user:
        print("Bot: My name is Bot. What is your name?")

        name = input("You: ")
        print("Bot: Nice name,", name)

    # How are you
    elif "how are you" in user:
        print("Bot: I am fine. What about you?")

        reply = input("You: ")
        print("Bot: Nice!")

    # Exit
    elif user == "bye":
        print("Bot: Goodbye!")
        break

    # Default
    else:
        print("Bot: Sorry, I don't understand.")