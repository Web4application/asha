from core.voice import listen, speak
from core.brain import detect_intent
from system.files import handle_files
from memory.memory import handle_memory
from core.emotions import handle_emotion

def main():
    speak("ASHA online. I'm listening.")

    while True:
        text = listen()
        if not text:
            continue

        intent = detect_intent(text)

        if intent == "system":
            handle_files(text)

        elif intent == "memory":
            handle_memory(text)

        elif intent == "emotion":
            handle_emotion()

        else:
            speak("I heard you.")
