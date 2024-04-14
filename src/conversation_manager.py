import os
from openai import OpenAI
from event_handler import EventHandler

class ConversationManager():
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.client = OpenAI(api_key = self.api_key)
        
    def conversation(self) -> None:

        gpt_assistant_prompt = "You are Jarvis, the virtual assistant from Iron Man, you are here to help. You should use the language that Jarvis uses, and act like it. Pretend I'm Tony Stark, but my name is Lucas Coelho."
        user_input = "Introduce yourself and be promt to answer further questions, after answering each question, be sure to ask if I need to know anything else. If my input is quit, please be sure to say goodbye propperly."

        message=[{"role": "assistant", "content": gpt_assistant_prompt}, 
                 {"role": "user", "content": user_input}]
        
        temperature=0.2
        max_tokens=256
        frequency_penalty=0.0
        
        response = self.client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = message,
                temperature = temperature,
                max_tokens = max_tokens,
                frequency_penalty = frequency_penalty
            )
        
        print(response.choices[0].message.content)
        message.append({"role": "assistant", "content": response.choices[0].message.content})
        
        while user_input != "quit":
            
            user_input = input("\n> ")
            message.append({"role": "user", "content": user_input})

            response = self.client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = message,
                temperature = temperature,
                max_tokens = max_tokens,
                frequency_penalty = frequency_penalty
            )
            
            print("\n" + response.choices[0].message.content)
            message.append({"role": "assistant", "content": response.choices[0].message.content})
    
    def chat_assistant(self, user_input):
        
        assistant = self.client.beta.assistants.create(
            name="Jarvis",
            instructions="You are Jarvis, the virtual assistant from Iron Man, you are here to help me code in various programming. You should use the language that Jarvis uses, and act like it.",
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo",
            )

        thread = self.client.beta.threads.create()
            
        message = self.client.beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = user_input
            )
            
        with self.client.beta.threads.runs.stream(
            thread_id = thread.id,
            assistant_id = assistant.id,
            event_handler = EventHandler(),
            additional_messages = message
        ) as stream:
            stream.until_done()
            