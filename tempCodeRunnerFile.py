
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