# importers
import speech_recognition as srec
import pyttsx3

# Listener
listener = srec.Recognizer()
engine = pyttsx3.init()

# To Set Female Voice - 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Hola SwethAI
def welcome():
    engine.say('Bonjour, Blesslin ')
    engine.say(' Order me ')
    engine.say(' Master Jerry ')
    engine.runAndWait()


# SwethAI Echo
def echo(text):
    engine.say(text)
    # print(text)
    engine.runAndWait()


def order():
    try:
        with srec.Microphone() as me:
            print('I am all ears ...')
            voice = listener.listen(me)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'jerry' in cmd:
                cmd = cmd.replace('jerry', '')
                echo(cmd)

    except Exception as e:
        print(e)
        pass
    return cmd


def executor():
    cmd = order()
    # print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', 'playing')
        echo(song)


executor()
