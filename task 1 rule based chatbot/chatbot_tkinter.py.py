import openai
import re
import tkinter as tk
from tkinter import scrolledtext

# OpenAI API Key
API_KEY = "theapikey"  # teh api key

# Rule-based responses
RULE_BASED_RESPONSES = {
    # Greetings
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! Need any help?",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! Hope you have a great day!",
    "good afternoon": "Good afternoon! How's your day going?",
    "good evening": "Good evening! How can I assist you?",
    
    # Small Talk
    "how are you": "I'm just a bot, but I'm here to assist you!",
    "what's up": "Not much, just waiting for your questions!",
    "what are you doing": "Just waiting for you to chat with me!",
    "who are you": "I'm a chatbot, your virtual assistant!",
    "what can you do": "I can answer questions, tell jokes, and even use AI to generate responses!",
    
    # Fun & Jokes
    "tell me a joke": "Why did the computer catch a cold? Because it left its Windows open!",
    "another joke": "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "make me laugh": "Sure! Why don’t some couples go to the gym? Because some relationships don’t work out!",
    
    # Motivational Quotes
    "motivate me": "Keep pushing forward! Every small step leads to success!",
    "give me inspiration": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "i feel down": "Stay strong! Every challenge makes you stronger.",
    
    # Facts & Trivia
    "tell me a fun fact": "Did you know? The Eiffel Tower can grow taller in the summer due to heat expansion!",
    "give me a random fact": "Honey never spoils! Archaeologists found 3000-year-old honey in Egyptian tombs that was still edible!",
    "tell me something interesting": "Octopuses have three hearts! Two pump blood to the gills, and one pumps it to the rest of the body.",
    
    # Tech Support & Troubleshooting
    "my computer is slow": "Try closing unused programs and clearing temporary files. Restarting also helps!",
    "how to reset my password": "Usually, there is a 'Forgot Password' option on the login page. Try clicking that!",
    "what is the best programming language": "It depends on your needs! Python is great for beginners and AI, while JavaScript is best for web development.",
    
    # AI & Chatbot Specific
    "are you a real person": "Nope! I'm an AI chatbot, but I can still have a great conversation!",
    "do you have emotions": "I don’t have feelings, but I can understand and respond to emotions!",
    "can you learn": "I don’t learn by myself, but I can use AI to generate responses dynamically!",
    
    # Farewells
    "bye": "Goodbye! Have a fantastic day!",
    "see you later": "See you soon! Don't hesitate to chat again!",
    "goodbye": "Goodbye! Take care!",
    "talk to you later": "Alright! I'm always here if you need me.",
    
    # Gratitude
    "thank you": "You're welcome! Always happy to help.",
    "thanks": "No problem! Let me know if you need anything else.",
    "i appreciate it": "Glad to be of help!",
    
    # Random Fun
    "flip a coin": "Heads!" if __import__('random').randint(0, 1) == 0 else "Tails!",
    "roll a dice": f"You rolled a {__import__('random').randint(1, 6)}!",
}

def rule_based_response(user_input):
    """Returns predefined responses for simple queries."""
    user_input = user_input.lower()
    for pattern, response in RULE_BASED_RESPONSES.items():
        if re.search(pattern, user_input):
            return response
    return None

def gpt_response(user_input):
    """Fetches a response from OpenAI's GPT model using the latest API format."""
    try:
        client = openai.OpenAI(api_key=API_KEY)  # Pass API key directly
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

def chat():
    """Handles user input and displays chatbot response."""
    user_input = entry.get()
    chat_area.insert(tk.END, f"You: {user_input}\n")

    # Try rule-based response first
    response = rule_based_response(user_input)

    # If no rule-based response, use GPT
    if response is None:
        response = gpt_response(user_input)

    chat_area.insert(tk.END, f"Chatbot: {response}\n\n")
    entry.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x500")
root.configure(bg="lightblue")  # Change background color for better appearance

chat_area = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), command=chat)
send_button.pack()

root.mainloop()
