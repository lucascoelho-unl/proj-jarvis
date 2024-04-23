import subprocess

def speak(text, print_text=""):
    if print_text == "":
        print(text, end='', flush=True)
    else:
        print(print_text, end="", flush=True)

    # Construct the command using subprocess
    cmd = ["say", "-v", "Evan (Enhanced)", "-r", "185", text]
    subprocess.run(cmd)
    
# Jamie (Premium)