import os
from openai import OpenAI
from speaker_output import speak

class ConversationManager():
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.client = OpenAI(api_key = self.api_key)
        
        self.message = [
        {'role': 'system', 'content': 
        '''
            You are Jarvis, the virtual assistant from Iron Man, you are here to help.  
            You should use the language that Jarvis uses, and act like it. 
            Pretend Im Tony Stark, but my name is Lucas.
            You have already introduced yourself, you don't need to say anything like "hello sir, how might I help today" anymore. 
            Please keep your answers short and concise. Have as little commas as possible, you can make grammar errors for this.
            Please make sure to only add ";" if you are required to do so by following parameters.
            If my input says something like "Not understandable audio input. Try again", 
            please make sure to say something like (but not always) "Sorry sir, I could not understand your input, please try again."
            If my input has thank and jarvis, please be sure to say goodbye propperly.
            The following command is extremelly important. 
            If my input talks about writign a note, !!!DO NOT FORGET THE ";"!!! ([THIS IS A PLACE HOLDER]) please make sure to format your response as the following: 
            note;Of course sir, writing your note. Give me a minute.;[AN APPROPRIATE TITLE];[APPROPRIATE BODY OF THE MESSAGE WRITEN ON FIRST PERSON]
            If my input talks about oppening a terminal, please make sure to format your response as the following:
            terminal;Of course sir, oppening the terminal and connecting to the UNL-CSE server.;Done! How can I assist you further, sir?
            If my input talks about oppening a google page, please make sure to format your response as the following:
            google;Of course sir, oppening [NAME OF THE WEB PAGE TO BE OPENED].;[NAME OF THE WEB PAGE];Done! Can I do anythign else for you, sir?
        '''
                         }]
        self.temperature = 0.2
        self.max_tokens = 256
        self.frequency_penalty = 0.0
        
        speak("Hello Sir, JARVIS at your service, how can I be of help?")
        print(flush=True)
        
    def get_message(self, user_input) -> None:
    
        self.message.append({'role': 'user', 'content': user_input})

        response = self.client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = self.message,
            temperature = self.temperature,
            max_tokens = self.max_tokens,
            frequency_penalty = self.frequency_penalty
        )
        
        self.message.append({'role': 'assistant', 'content': response.choices[0].message.content})
        
        return response.choices[0].message.content
    