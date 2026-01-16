import ollama

print("Enter a prompt or /quit to exit")
messageHistory = []

userInput = None

while userInput != "/quit":
    userInput = input("You: ")
    messageHistory.append({"role": "user", "content": userInput})
    response: ollama.ChatResponse = ollama.chat(model = "llama3.2:3b", messages = messageHistory, stream = True)
    streamedResponse = ""
    for chunk in response:
        print(chunk.message.content, end = "", flush = True)
        streamedResponse += chunk.message.content
    messageHistory.append({"role": "assistant", "content": streamedResponse})
    if len(messageHistory) > 10:
        messageHistory.pop(0)
    print()
