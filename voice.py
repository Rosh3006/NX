import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from information import infow
from song import  music
from audionews import *
from ss import *
import randfacts
from fun import *
import datetime


engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>12 and hour<16:
        return("afternoon")
    else:
        return("evening")

r = sr.Recognizer()
speak("Hello ,Good"+ wishme()+"your voice Assistant is here.")
speak("Today is "+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+(today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
speak("How are you")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am  also having a good day")
speak("What can I do for you??")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening....')
    audio=r.listen(source)
    text2=r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening')
        audio=r.listen(source)
        infor=r.recognize_google(audio)
        print("searching {} in wikipedia".format(infor))
        speak("searching {} in wikipedia".format(infor))
        assist=infow()
        assist.get_info(infor)  

elif "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio=r.listen(source)
        vid=r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        speak("Playing {} on youtube".format(vid))
        assist=music()
        assist.play(vid) 

elif "news" in text2:
    print("Sure,Now I will read news for you")
    speak("Sure,Now I will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif 'fact' in text2:
    speak("Sure")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that"+x)

elif "joke"  in text2:
    speak("Sure get ready for some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
        
    
