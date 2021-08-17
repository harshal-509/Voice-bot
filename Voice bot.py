import os
import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Sir!")
    elif(hour>=12 and hour<=4):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Jarvis at your Service!")
def task():
    recognize=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.......")
        recognize.adjust_for_ambient_noise(source)
        recognize.pause_threshold=1
        audio=recognize.listen(source)
    try:
        print("Analyzing.......")
        query=recognize.recognize_google(audio,language="en-in")
        print(f"{query}\n")
    except:
        print("Unable to understand......")
        return "None"
    return query
wish()
while(1):
    q=task().lower()
    if("wikipedia" in q):
        speak("Searhing.......")
        q=q.replace("wikipedia","")
        results=wikipedia.summary(q,sentences=2)
        speak("According to Wikipidea")
    elif("open youtube" in q):
        webbrowser.open("youtube.com")
    elif("open google" in q):
        webbrowser.open("google.com")
    elif("open leetcode" in q):
        webbrowser.open("leetcode.com")
    elif("time" in q):
        current=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,its {current}")
    elif("quit" in q):
        speak("Have a nice day Sir!")
        exit(0)
    """
    elif("play music" in q):
        music="C:\\Users\\wwwhs\\OneDrive\\Documents\\python\\1. Recursion 1"
        songs=os.listdir(music)
        os.startfile(os.path.join(music,songs[0]))
    elif ("open code" in q):
        Code="C:\\src\\projects\\New folder\\Untitled-1.py"
        os.startfile(Code)
    """