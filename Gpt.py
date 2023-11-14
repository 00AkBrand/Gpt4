import openai

# Set your OpenAI API key
openai.api_key = 'AK Brand'

# Function to interact with the GPT-3 model
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the engine you want to use
        prompt=prompt,
        max_tokens=150  # You can adjust the maximum number of tokens in the response
    )
    return response.choices[0].text.strip()

# Example conversation
conversation_history = "Hello, how can I assist you today?"

while True:
    user_input = input("You: ")
    conversation_history += "\nYou: " + user_input

    # Generate GPT-3 response
    gpt_response = chat_with_gpt(conversation_history)

    # Print GPT-3 response
    print("ChatGPT:", gpt_response)

    # Update conversation history
    conversation_history += "\nChatGPT: " + gpt_response