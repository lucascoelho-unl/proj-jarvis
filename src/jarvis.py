import os
import time
from conversation_manager import ConversationManager
from event_handler import handle_response
from audio_input import get_audio_input
from speaker_output import speak
from dotenv import load_dotenv

load_dotenv()

os.system('cls|clear')

cm = ConversationManager(os.getenv('JARVIS_API_KEY'))
cm.initialize()

user_input = ''

while ('thank' not in user_input.lower()) or ('jarvis' not in user_input.lower()):
    #user_input = get_audio_input()
    user_input = input()
    response = cm.get_message(user_input)
    handle_response(response)
    print()
