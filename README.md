# Simple Rule-Based Chatbot

## 1. Project Overview
This project implements a simple rule-based chatbot using Python. The chatbot interacts through the console, recognizes predefined user intents through pattern matching, responds using rule-based logic, and maintains a small knowledge base for domain-specific answers. It also logs conversations for documentation and evaluation. The goal is to help beginners understand core concepts of AI and NLP.

## 2. Key Features
- Rule-based intent detection
- Domain knowledge base (OSI, TCP/UDP, routers, switches)
- Conversation logging to chat_history.txt
- Easy to extend with new intents and responses
- No external libraries required


## 4. How the Chatbot Works
1. User enters a text message.
2. The program detects the intent using basic pattern rules.
3. The chatbot responds based on:
   - Matching rule
   - Knowledge base
   - Fallback response
4. Every message is stored in a conversation log.

## 5. How to Run the Project
1. Make sure Python 3.x is installed.
2. Open the project folder.
3. Launch Command Prompt in the folder.
4. Run:

python simple_chatbot.py


## 6. Sample Commands
- hi
- help
- who are you
- osi layers
- tcp udp difference
- what is router
- bye


Created for educational use as a demonstration of fundamental AI and NLP concepts.
