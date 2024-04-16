import os
from conversation_manager import ConversationManager
from audio_input import get_audio_input
from speaker_output import speak
from dotenv import load_dotenv

load_dotenv()

os.system('cls|clear')

cm = ConversationManager(os.getenv('JARVIS_API_KEY'))

user_input = ''

while ('thank' not in user_input.lower()) or ('jarvis' not in user_input.lower()):
    user_input = get_audio_input()
    response = cm.get_message(user_input)
    print('\n' + response)
    speak(response)
