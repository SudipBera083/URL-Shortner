# URL-Shortner

import pyshorteners

import pyttsx3

import speech_recognition as sr




engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# print(voices)

engine.setProperty('voice', voices[1].id)


def speak(audio):

    engine.say(audio)
    
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as m:
    
        print("Listening...")
        
        r.pause_threshold=1
        
        audio = r.listen(m)

    try:
    
      print("Recognizing...")
      
      query = r.recognize_google(audio, language="eng-in")
      
      print(f"User Said:{query}\n")

    except Exception as e:
    
        # print(e)

        print("Say that again Please...")
        
        return  "None"

    return  query


def Shortner():

    speak("Please Paste the Url sir")
    
    s = pyshorteners.Shortener()
    
    url = input("Enter the Url Sir!")
    
    try:
    
        speak("The URL is shorted successfully !")
        
        print("The short URL is ", s.dagd.short(url))
        

    except:
    
        speak("Enter the valid URL!")
        
        print("Enter the valid URL!")


if __name__ == '__main__':

    speak("Welcome to your smart program sir!")
    
    query = takeCommand()
    
    if "the URL shortener" in query:
    
        Shortner()

