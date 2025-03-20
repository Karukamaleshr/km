import pyttsx3
import speech_recognition as sr
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)  
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Check your internet connection.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def tutor_flow():
    webbrowser.open("https://meet.tutor.com/")   #replace with tutor link
    speak("Welcome to the AI Tutor platform!")

    # Step 1: Ask if they want to navigate
    speak("Do you want to navigate to the next page? Say yes or no.")
    command = listen()

    if command and "yes" in command:
        speak("Navigating to the next page.")

        # Step 2: Ask for subject
        speak("What subject do you study? Say Physics, Maths, or Biology.")
        command = listen()                 #fill subject name here in frontend and subject name is stored in command

        tutors = {
            "physics": "Mrs. Anitha",
            "maths": "Mrs. Dhanalakshmi",
            "biology": "Kunju Mani"
        }

        if command in tutors:
            tutor_name = tutors[command]
            speak(f"For {command}, your available tutor is {tutor_name}.")
                #display tutor name in frontend

            # Step 3: Ask if they want to join Google Meet
            speak("Do you want to continue into Google Meet? Say yes or no.")
            command = listen()

            if command and "yes" in command:
                speak("Opening Google Meet.")
                webbrowser.open("https://meet.google.com/")  # replace with your google meet link if u want
            else:
                speak("Exiting.")
        else:
            speak("Sorry, I didn't understand the subject.")
    else:
        speak("Exiting.")

# Start listening for "tutor"
print("Say 'tutor' to begin.")
speak("Say 'tutor' to begin.")

while True:
    command = listen()
    if command and "tutor" in command:
        tutor_flow()
        break
