import json
from voice import speak

MEMORY_FILE = "memory.json"

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def handle_command(text):
    mem = load_memory()

    if "your name" in text:
        speak("My name is ASHA.")

    elif "remember that" in text:
        fact = text.replace("remember that", "").strip()
        mem["facts"].append(fact)
        save_memory(mem)
        speak("Got it. I will remember that.")

    elif "what do you remember" in text:
        if mem["facts"]:
            speak("Here is what I remember.")
            for f in mem["facts"]:
                speak(f)
        else:
            speak("I don't remember anything yet.")

    elif "hello" in text:
        speak("Hello. I'm here with you.")

    elif "stop" in text or "exit" in text:
        speak("Goodbye.")
        exit()

    else:
        speak("I heard you, but I don't understand yet.")
