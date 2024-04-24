from speaker_output import speak
import auto_guide
import utils

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
    
    elif processed_text[0] == 'weather':
        print(flush=True)
        weather_info = utils.get_weather(processed_text[1])
        speak(weather_info)

    elif processed_text[0] == 'calendar':
        print(flush=True)
        speak("Of course, Sir! Setting up event in your Apple Calendar.")
        auto_guide.create_calendar_event(processed_text[1])
        print(flush=True)
        speak("Done, you can now see the event in your calendar. Can I help with anything else, sir?")
    
    else:
        print(flush=True)
        speak(processed_text[0], print_text=processed_text[0])
