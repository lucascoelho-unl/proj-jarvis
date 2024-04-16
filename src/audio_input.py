import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 10000

def capture_voice_input():
    with sr.Microphone() as source:
        print("\n> ", end='')
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(text)
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
