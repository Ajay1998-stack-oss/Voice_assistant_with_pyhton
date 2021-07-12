import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say('Hello, Ajaaay I am your Voice recorgenization system Alexa.. ')
    engine.say('What can i do for you')
    engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass
