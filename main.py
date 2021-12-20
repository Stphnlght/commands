# Importing required modules
# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing os module
import os


# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            query = r.recognize_google(audio)
            print("the query is ", query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return query


# creating Speak() function to giving Speaking power
# to our voice assistant
def speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


activate = take_commands()
if "light" in activate:
    speak("yes, what can I do for you?")
    while True:
        command = take_commands()
        if "sleep" in command:
            speak("OK, sleeping")
            os.system("shutdown /l /t 30")
            break
        if "restart" in command:
            speak("OK, Restarting")
            os.system("shutdown /r /t 30")
            break
        if "shutdown" in command:
            speak("OK, shutting down")
            os.system("shutdown /s /t 30")
            break
        speak("sorry, I don't recognize your command, please come again")
