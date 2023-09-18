#The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

import os 
# import wikipedia
import wikipedia
#import datetime
import datetime
# os.system('cls')
import pyttsx3
#import speech_recognition
import speech_recognition as sr
#import webbrowser
import webbrowser 
# this is used for voices 
# in window we have in built voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
# here we set property of voice as male voice 
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio) 

    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am a jarvis sir! how may i help you ! ")

def takecommand():
    # It takes microphone input from use and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
# threshold is use to take space in speaking if am speaking something and take a few second pause then recognizing didn't it take a few second for listening
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    speak("hello zaaid how are you")
    wishme()
    while True:
    # if 1:
        query = takecommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open Whatsapp' in query:
            webbrowser.open("https://www.whatsapp.com")
        elif 'open snapchat' in query:
            webbrowser.open("https://www.snapchat.com")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instgram.com")
        elif 'open wikipedia broswer' in query:
            webbrowser.open("https://www.wikipedia.com")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ! the time is {strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\zayni\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)