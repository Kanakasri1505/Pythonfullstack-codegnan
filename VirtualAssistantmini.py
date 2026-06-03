import pyttsx3  #text to speech convert
import speech_recognition as sr  #to recognise the speech
import datetime #to calculate date and time at the instant
import webbrowser
import wikipedia


def speak(text):
    engine=pyttsx3.init()#initialize voice engine (engine is just a variable)

    engine.say(text)
    engine.runAndWait()
    del engine

def take_command():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You Said: ",command)
        return command.lower()
    
    except Exception:
        print("Sorry, Please Say that again.")
        return ""
    
def greet_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning \n I Am Your Virtual Assistant")

    elif hour < 18:
        speak("Good Afternoon \n I Am Your Virtual Assistant")

    else:
        speak("Good Evening \n I Am Your Virtual Assistant")


greet_user()

while True:

    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

   

    elif "exit" in command:
        speak("Goodbye")
        break
    

        

        
    
