import os
from conversation_manager import ConversationManager
from dotenv import load_dotenv

load_dotenv()

os.system("cls|clear")

cm = ConversationManager(os.getenv("JARVIS_API_KEY"))

user_input = ""

while user_input != "quit":
    user_input = input("\n> ")
    response = cm.conversation(user_input)
    print("\n" + response)
