import os
from conversation_manager import ConversationManager
from audio_manager import get_audio_input
from speaker_manager import speak
from dotenv import load_dotenv

load_dotenv()

os.system("cls|clear")

cm = ConversationManager(os.getenv("JARVIS_API_KEY"))

user_input = ""

while "quit" not in user_input:
    user_input = get_audio_input()
    response = cm.get_message(user_input)
    print("\n" + response)
    speak(response)
