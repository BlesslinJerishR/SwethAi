import speech_recognition as srec
import pyttsx3

listener = srec.Recognizer()
engine = pyttsx3.init()


# To Set Female Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def order():
    try:
        with srec.Microphone() as me:
            print('I ma all years ...')
            voice = listener.listen(me)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'jarvis' in cmd:
                print(cmd)
    except:
        pass
    return cmd


engine.say('Bonjour, Blesslin')
engine.say('Order me')
engine.say('Master Jerry')
engine.runAndWait()



