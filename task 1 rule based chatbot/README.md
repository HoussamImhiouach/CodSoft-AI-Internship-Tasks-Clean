# Chatbot with Rule-Based Responses

## Overview

This project is a chatbot that responds to **predefined rule-based queries**. If the user asks something not covered by predefined rules, the chatbot **calls OpenAI's API** (GPT-3.5-Turbo) to generate an appropriate response. The chatbot runs on a **GUI-based interface using Tkinter**.

## How It Works

1. **Rule-Based Responses**
   - If the user's input matches predefined responses, the chatbot replies immediately.
2. **GPT-3.5 Integration**
   - If no match is found, the chatbot sends the input to OpenAI’s API for an AI-generated response.
3. **GUI Interface**
   - Users enter text into a Tkinter GUI, and responses are displayed in a text area.

## Technologies Used

- **Python**
- **Tkinter (GUI)**
- **OpenAI API (GPT-3.5 Turbo)**
- **Regex (Pattern Matching for Rule-Based Responses)**

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Internship-Tasks.git
   cd AI-Internship-Tasks/chatbot
   ```
2. **Install dependencies:**
   ```bash
   pip install openai
   ```
3. **Run the script:**
   ```bash
   python chatbot_tkinter.py
   ```

## Usage Guide

1. Open the chatbot GUI.
2. Type a message (e.g., `"Hello"` or `"Tell me a joke"`).
3. If it's a predefined message, the chatbot responds immediately.
4. Otherwise, OpenAI GPT-3.5 generates a response.

## Expected Output

```
User: "Hello"
Chatbot: "Hello! How can I assist you today?"

User: "Tell me a joke"
Chatbot: "Why do programmers prefer dark mode? Because the light attracts bugs!"
```

## Future Improvements

- Add **speech-to-text** input.
- Store **chat history** for user reference.
- Integrate **voice response** using text-to-speech.

## License

This project is open-source and available under the MIT License.
