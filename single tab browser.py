import pyttsx3
import speech_recognition as sr
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Reusable function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Define keywords and their corresponding links
commands = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com"
}

def listen():
    """Function to capture voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=4)  # 4-second timer
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Could not request results. Check your internet.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def voice_command_listener():
    """Main function that listens for keywords and performs actions."""
    activated = False  # Activation flag

    # Prompt only once for activation
    print("Say 'Ok Superman' to activate.")
    speak("Say 'Ok Superman' to activate.")
    
    while not activated:
        command = listen()
        if command == "ok superman":
            activated = True
            speak("Voice link opener activated.")
            print("Activation successful. You can now say a keyword.")

    # Open an initial tab to reuse
    first_url = list(commands.values())[0]
    webbrowser.open(first_url, new=0)  # Opens first link in same tab

    # After activation, continuously listen for commands
    while True:
        print("Waiting for a command...")
        command = listen()

        if command in commands:
            speak(f"Opening {command}")
            webbrowser.open(commands[command], new=0)  # Open in same tab
        
        elif command == "exit superman":
            speak("Goodbye, shutting down.")
            print("Exiting...")
            break

# Start the program
voice_command_listener()
