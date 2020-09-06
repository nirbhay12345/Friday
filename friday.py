import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

def speak(audio):
    voices = engine.getProperty('voices')# getting details of current voices
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female and 0 for male
    engine.say(audio) # used to say something
    #engine.save_to_file("hello everyone", 'test.mp3') #used to store voice in a file
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is ")
    speak(Time)

def date():
    mon = {1:"January", 2:"Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    year = int(datetime.datetime.now().year)
    num = int(datetime.datetime.now().month)
    month = mon[num]
    day = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir")
    speak("Friday at your service! What would you like to do?")

# wishme()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\foopc\\Desktop\\friday\\ss.png")

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hereicomethedanger@gmail.com', 'abcd')
    server.sendmail('hereicomethedanger@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 2000
        audio = r.listen(source, timeout=20)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Could not hear you, say that again please")
        return "None"
    
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery = psutil.sensors_battery()
    speak("The battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    # print(sr.Microphone().list_microphone_names())# gives the list of all the microphones
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif ('date'or'day') in query:
            date()
        
        elif 'wikipedia' in query:
            try:
                speak("Searching....")
                query = query.replace('Wikipedia', '')
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("Could not find " + query + " on wikipedia, try something else")
        
        elif 'send email' in query:
            try:
                speak("To whom should i send the email?")
                to = takeCommand()
                speak("What should i say?")
                content = takeCommand()
                sendMail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Email could not be send")
        
        elif 'search in chrome' in query:
            speak("What should i search for?")
            chromePath = "C:/Users/foopc/AppData/Local/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search + '.com')

        elif 'screenshot' in query:
            screenshot()
            speak("Taken!!!")

        elif 'logout' in query:
            os.system("shutdown -l")

        elif "how are you" in query:
            speak("I m fine, How are you? Do you want me to help you any way?")

        # elif 'friday play songs' in query:
        #     songs_dir = ''
        #     songs = os.listdir(songs_dir)
        #     os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("You have told me to remember that "+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you remember' in query:
            data = open('data.txt', 'r')
            speak("you told me to remember that "+data.read())

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Signing off sir!")
            speak("Take care sir")
            quit()












# Coding Extras


# rate = engine.getProperty('rate') # getting details of current speaking rate
# engine.setProperty('rate', 200)     # setting up new voice rate
# volume = engine.getProperty('volume')  #getting details of current volume
# engine.setProperty('volume', 1.0)  # setting up new volume