import pyautogui
import time
import os
from dotenv import load_dotenv

def write_note_in_notes_app(title, body):
    # Open notes app
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    pyautogui.typewrite("notes")
    pyautogui.press('enter')
    time.sleep(2)

    # Create a new note
    pyautogui.keyDown('command')
    pyautogui.press('n')
    pyautogui.keyUp('command')
    pyautogui.typewrite(title)
    pyautogui.press('enter')
    pyautogui.typewrite(body)

    # Close Notes
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')

def connect_to_terminal_cse_server():
    load_dotenv()

    # Open the terminal
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    pyautogui.typewrite("terminal")
    pyautogui.press('enter')
    time.sleep(2)

    # Log into the server
    pyautogui.typewrite("ssh lmoreiradesouzacoe2@cse-linux-01.unl.edu")
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite(os.getenv('UNL_CSE_PASSWORD'))
    pyautogui.press('enter')

def open_web_page(page_name):
    # Opening google
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    pyautogui.typewrite("google")
    pyautogui.press('enter')
    time.sleep(1)

    # Open new tab
    pyautogui.keyDown('command')
    pyautogui.press('t')
    pyautogui.keyUp('command')

    # Search for web page
    pyautogui.typewrite(page_name)
    pyautogui.press('enter')