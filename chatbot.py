import re
def chatbot():
    print("Chatbot: Hi, I'm your customized chatbot. How can I assist you today?")
     while True:
        user_input = input("You: ").lower()
if re.search(r"\b(hello|hi)\b", user_input):
            print("Chatbot: Hello there! What can I help you with today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm doing well, thanks for asking! How can I assist you?")
        elif re.search(r"your name", user_input):
            print("Chatbot: I'm an enhanced rule-based chatbot, here to assist you.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Hope to chat again soon!")
            break
        else:
            print("Chatbot: Hmm, I'm not sure about that. Could you rephrase?")
chatbot()
