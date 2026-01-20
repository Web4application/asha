from core.voice import listen, speak
from core.brain import think
from core.intents import detect_intent
from security.permissions import requires_confirmation
from tools.browser import open_site
from memory.longterm import remember
from core.emotions import respond_with_mood

def main():
    speak("ASHA online. Full systems ready.")

    while True:
        text = listen()
        if not text:
            continue

        if "exit" in text:
            speak("Shutting down.")
            break

        if requires_confirmation(text):
            speak("Confirm this action.")
            if "yes" not in listen():
                speak("Action cancelled.")
                continue

        intent = detect_intent(text)

        if intent == "browser":
            speak("Opening browser.")
            open_site("https://google.com")

        elif intent == "memory":
            remember(text)
            speak("Saved to memory.")

        else:
            reply = think(text)
            speak(respond_with_mood(reply))

if __name__ == "__main__":
    main()
