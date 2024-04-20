from speaker_output import speak
import auto_guide

def handle_response(text):
    processed_text = text.split(";")
        
    if processed_text[0] == "note":
        print(flush=True)
        speak(processed_text[1])
        auto_guide.write_note_in_notes_app(processed_text[2], processed_text[3])
        print(flush=True)
        speak("Done! How might I assist you further?")

    elif processed_text[0] == 'terminal':
        print(flush=True)
        speak(processed_text[1])
        auto_guide.connect_to_terminal_cse_server()
        print(flush=True)
        speak(processed_text[2])

    elif processed_text[0] == 'google':
        print(flush=True)
        speak(processed_text[1])
        auto_guide.open_web_page(processed_text[2])
        print(flush=True)
        speak(processed_text[3])
    
    else:
        print(flush=True)
        new_text = processed_text[0].replace(",","")
        speak(new_text, print_text=processed_text[0])
        