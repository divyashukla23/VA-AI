from gtts import gTTS
import webbrowser
import os
import wikipedia
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
import yaml
import random
with open("ds.yml", 'r') as stream:
    try:
        y = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
data = dict()
for i in y['conversations']:
    data[i[0]] = data.get(i[0],i[1:])

while 1:
    engine.say("Hi dear, why do u need me?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        inp = r.recognize_google(audio)
    except:
        continue

    q = 0
    if inp == "stop":
        engine.say("its hard letting you go but see you soon mam")
        break
    elif "what is" in inp:
        b = inp.split("what is")
        try:
            Divy = wikipedia.summary(b[1],sentences=3)
            q = 1
        except:
            q = 0
    else:
        if(inp in data.keys()):
            Divy = random.choice(data['inp'])
            q = 1
            break
    if q == 0:
        Divy = "what is that i really dont know !!! "
    print(Divy)
    engine.say(Divy)
engine.runAndWait()