import google.generativeai as genai
import pyttsx3

def speak(text, voice_id=0, rate=150):
    engine = pyttsx3.init()

    # Set voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)

    # Set speech rate
    engine.setProperty('rate', rate)

    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, how can I assist you?", voice_id=1, rate=180)  # Change voice and speed
# Configure your API key
api_key = input("Enter your Gemini API key: ")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-pro-exp')
# Chat loop
print("\nWelcome to Doubt Session! Say 'exit' to end the conversation.\n")
speak("Welcome to Doubt Session! Say 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
    
    try:
        response = model.generate_content(user_input)
        print(f"AI: {response.text}\n")
        speak(response.text, voice_id=1, rate=180)  # Change voice and speed
    except Exception as e:
        print(f"Error: {str(e)}")