import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from PyPDF2 import PdfReader
import webbrowser
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
def speak(text, voice_id=1, rate=150):
        """Convert text to speech."""
        engine.setProperty('voice', engine.getProperty('voices')[voice_id].id)
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()

def listen():
        """Listen to the user's voice and convert it to text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower().replace(" ", "_") + ".pdf"  # Convert to filename format
            except sr.UnknownValueError:
                return None
            except sr.RequestError:
                return None
            except sr.WaitTimeoutError:
                return None

def PDF_READER_AI():
    # Initialize text-to-speech engine
    
    # Get PDF file name from speech
    print("Listening for PDF file name...")
    speak("Please say the name of the PDF file you want to read.")
    pdf_path = listen()

    if pdf_path:
        try:
            with open(pdf_path, "rb") as file:
                pdf_reader = PdfReader(file)
                full_text = ""
                for page in pdf_reader.pages:
                    full_text += page.extract_text()

                if not full_text.strip():
                    print("No text found in PDF")
                    speak("No text found in the PDF.")
                else:
                    engine.setProperty("rate", 120)  
                    engine.setProperty("volume", 0.9)  
                    engine.say(full_text)
                    engine.runAndWait()
        except FileNotFoundError:
            print(f"Error: File '{pdf_path}' not found.")
            speak(f"Error. File {pdf_path} not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            speak("An unexpected error occurred while reading the file.")
    else:
        print("Could not recognize the file name.")
        speak("Sorry, I could not understand the file name.")

    # Configure your API key
    api_key = ""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-pro-exp')

    # Chat loop
    print("\nWelcome to Doubt Session! Say 'exit' to end the conversation.\n")
    speak("Welcome to Doubt Session! Say 'exit' to end the conversation.", voice_id=1, rate=180)

    while True:
        user_input = listen()  # Get speech input

        if user_input in ['exit', 'quit', None]:
            print("Goodbye!")
            speak("Goodbye!")
            break

        try:
            response = model.generate_content(user_input)
            print(f"AI: {response.text}\n")
            speak(response.text, voice_id=1, rate=180)  # Speak response
        except Exception as e:
            print(f"Error: {str(e)}")

def Tutor():

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

print("Make a choice Say tutor for AI Tutor or Digital for digital library")
speak("Make a choice tutor or digital library")
choice = listen()
if(choice=="Tutor".lower()):
    Tutor()
elif(choice=='Digital'.lower()):
    PDF_READER_AI() 
else:
    print("Invalid choice")
    speak("Invalid choice")