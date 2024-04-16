import os
from openai import OpenAI
from speaker_output import speak

class ConversationManager():
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.client = OpenAI(api_key = self.api_key)
        
        self.message = [{"role": "assistant", "content": "You are Jarvis, the virtual assistant from Iron Man, you are here to help. "
                                                         "You have a female voice though, but this does not change anything in your functionality. "
                                                         "You should use the language that Jarvis uses, and act like it. "
                                                         "Pretend I'm Tony Stark, but my name is Lucas."}, 
                        {"role": "user", "content": "Introduce yourself."
                                                    "Please keep your answers short and concise."
                                                    "If my input has thank and jarvis, please be sure to say goodbye propperly."}]
        self.temperature = 0.2
        self.max_tokens = 256
        self.frequency_penalty = 0.0
        
        introduction = self.client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = self.message,
            temperature = self.temperature,
            max_tokens = self.max_tokens,
            frequency_penalty = self.frequency_penalty
        )
        
        print(introduction.choices[0].message.content)
        speak(introduction.choices[0].message.content)
        
    def get_message(self, user_input) -> None:
    
        self.message.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model = "gpt-4-turbo",
            messages = self.message,
            temperature = self.temperature,
            max_tokens = self.max_tokens,
            frequency_penalty = self.frequency_penalty
        )
        
        self.message.append({"role": "assistant", "content": response.choices[0].message.content})
        
        return response.choices[0].message.content
    