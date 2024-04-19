import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import mac_say

def speak(text):
    print(text, end='', flush=True)
    # tts = gTTS(text=text, lang='en', tld='co.uk', slow=True)
    # filename = 'voice_output.mp3'
    # tts.save(filename)
    # playsound.playsound(filename)
    text_to_say = "say  -v Daniel " + text
    os.system(text_to_say)