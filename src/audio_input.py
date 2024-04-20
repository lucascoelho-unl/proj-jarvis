import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 15000
recognizer.pause_threshold = 1.2

def capture_voice_input():
    print("\n> ", end='', flush=True)
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(text, flush=True)
        return text
    except sr.UnknownValueError:
        text = ""
        return "Not understandable audio input. Try again"
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


def get_audio_input():
    audio = capture_voice_input()
    text = convert_voice_to_text(audio)
    return text
