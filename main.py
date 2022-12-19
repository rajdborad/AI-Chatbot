# import basic functions
import numpy as np

#for speach recognition
import speech_recognition as sr

# Beginning of AI

class ChatBot():
    def __init__(self, name):
        print("** Hello,",name,"**")
        self.name = name
    
    # speech to text function
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ",self.text)
        except:
            print("me --> ERROR")
    

    def wake_up(self, text):
        return True if self.name in text.lower() else False
        

#execute AI

if __name__ == "__main__":
    ai = ChatBot(name="Raj")
    while True:
        ai.speech_to_text()