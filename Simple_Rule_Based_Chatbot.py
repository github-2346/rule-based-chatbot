import re
from datetime import datetime

# ---------- Knowledge Base (Domain: Computer Networks) ----------

KNOWLEDGE_BASE = [
    {
        "keywords": ["osi", "layers of osi"],
        "answer": "The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application."
    },
    {
        "keywords": ["tcp", "udp", "difference between tcp and udp"],
        "answer": "TCP is connection-oriented and reliable, while UDP is connectionless and faster but unreliable."
    },
    {
        "keywords": ["ip address", "ipv4"],
        "answer": "An IPv4 address is a 32-bit number written as four decimal numbers (0–255) separated by dots, like 192.168.1.1."
    },
    {
        "keywords": ["router"],
        "answer": "A router is a networking device that forwards data packets between different networks."
    },
    {
        "keywords": ["switch"],
        "answer": "A switch is a device that connects devices within the same network and forwards frames based on MAC addresses."
    },
]

# ---------- Simple Rule-Based Responses for Intents ----------

GREETING_PATTERNS = [
    r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bhola\b", r"\bnamaste\b"
]

HELP_PATTERNS = [
    r"\bhelp\b", r"\bwhat can you do\b", r"\bhow to use\b", r"\boptions\b"
]

SMALL_TALK_PATTERNS = {
    r"\bhow are you\b": "I'm just a bunch of Python code, but I'm running fine! How can I help you today?",
    r"\bwho are you\b": "I'm a simple rule-based chatbot written in Python.",
    r"\bwhat is your name\b": "You can call me NetBot, your small computer networks assistant.",
}

GOODBYE_PATTERNS = [
    r"\bbye\b", r"\bexit\b", r"\bquit\b", r"\bsee you\b"
]

# ---------- Logging Utility ----------

LOG_FILE = "chat_history.txt"

def log_message(role: str, message: str) -> None:
    """
    Append a single message to the log file with a timestamp.
    role: 'User' or 'Bot'
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {role}: {message}\n")

# ---------- Intent Detection ----------

def matches_any_pattern(user_input: str, patterns) -> bool:
    """Return True if any regex pattern matches the user input."""
    for p in patterns:
        if re.search(p, user_input):
            return True
    return False

def check_small_talk(user_input: str):
    """Return a small-talk response if any pattern matches, else None."""
    for pattern, response in SMALL_TALK_PATTERNS.items():
        if re.search(pattern, user_input):
            return response
    return None

def search_knowledge_base(user_input: str):
    """
    Very simple keyword-based search in the knowledge base.
    Returns an answer string if something matches, else None.
    """
    text = user_input.lower()
    for item in KNOWLEDGE_BASE:
        for kw in item["keywords"]:
            if kw in text:
                return item["answer"]
    return None

# ---------- Chatbot Core Logic ----------

def get_bot_response(user_input: str) -> str:
    text = user_input.lower().strip()
    
    # 1. Goodbye intent
    if matches_any_pattern(text, GOODBYE_PATTERNS):
        return "Goodbye! It was nice chatting with you. 👋"
    
    # 2. Greeting intent
    if matches_any_pattern(text, GREETING_PATTERNS):
        return "Hello! 👋 I am a simple rule-based chatbot for basic computer networks questions. Ask me anything about OSI, TCP/UDP, routers, switches, etc. Type 'help' if you need options."
    
    # 3. Help intent
    if matches_any_pattern(text, HELP_PATTERNS):
        return (
            "I can do a few things:\n"
            "• Greet you (say hi/hello)\n"
            "• Answer small talk (try: 'who are you', 'how are you')\n"
            "• Answer simple computer networks questions (OSI layers, TCP vs UDP, routers, switches, IP address)\n"
            "• You can type 'bye' or 'exit' to end the chat."
        )
    
    # 4. Small talk intent
    small_talk_reply = check_small_talk(text)
    if small_talk_reply:
        return small_talk_reply
    
    # 5. Domain knowledge questions
    kb_answer = search_knowledge_base(text)
    if kb_answer:
        return kb_answer
    
    # 6. Fallback
    return (
        "I am not sure how to answer that yet.\n"
        "Try asking me about: OSI layers, TCP vs UDP, IP address, routers, or switches.\n"
        "You can also type 'help' to see what I can do."
    )

def chat_loop():
    print("NetBot: Hi! I'm a simple rule-based chatbot for computer networks.")
    print("NetBot: Type 'help' to see what I can do, or type 'bye' to quit.\n")
    
    while True:
        user_input = input("You: ")
        log_message("User", user_input)
        
        bot_reply = get_bot_response(user_input)
        print("NetBot:", bot_reply)
        log_message("Bot", bot_reply)
        
        # If the user said bye/exit, end the loop
        if matches_any_pattern(user_input.lower(), GOODBYE_PATTERNS):
            break

if __name__ == "__main__":
    chat_loop()