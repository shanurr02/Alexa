

import pyttsx3     # pip intall pyttsx3
import datetime    
import speech_recognition as sr # pip install speechRecognition
import wikipedia   # pip install wilkipedia
import webbrowser
import os

# sapi5 the technology for voice recognition and synthesis provided by Microsoft.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" I am Alexa Sir. Please tell me how may i help you ")


def takeCommand():
    # it takes microphone input from the user and returns string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1   # breaking in tone of 1 sec is possible
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n ")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


if __name__ == '__main__':
    speak("Shan is a good boy")
    wishme()
    while True:
        query = takeCommand().lower()

 # Logic for exwcuting task based on query
        if 'wikipedia' in query:
            speak('Searhing wikipedia...')
            query = query.replace("wikipeadia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'play music' in query:
            music_dir = 'F:\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S %p")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
    

        elif 'open code' in query:
            codePath = "C:\\Users\MCSS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'quit' in query:
            speak(f"Thankyou for using Alexa. Hope you enjoyed it.")
            exit()
            