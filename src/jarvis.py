import openai
import os
from conversation_manager import ConversationManager
from dotenv import load_dotenv

load_dotenv()

cm = ConversationManager(os.getenv("JARVIS_API_KEY"))

os.system("cls|clear")

cm.conversation()
