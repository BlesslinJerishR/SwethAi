# importers
import time

import speech_recognition as srec
import pyttsx3
import pywhatkit

# Listener
listener = srec.Recognizer()
engine = pyttsx3.init()

# SETTINGS
# Default SwethAI Voice
engine.setProperty('voice', engine.getProperty('voices')[0].id)

# Default SwethAI Speed
engine.setProperty('rate', engine.getProperty('rate') - 50)


# Voice Changer
# You can't change your Girlfriend's attitude at least change her gender
def voice_changer(n):
    print("""To Change The Vocal Cord of SwethAI
    [ 0 - Male      ] 
    [ 1 - Female    ]
    """)
    n = int(input("Choose : "))
    engine.setProperty('voice', engine.getProperty('voices')[n].id)


# Speed Changer
# You can't shut your Girlfriend's mouth at least control her speed
def speed_changer(n):
    print("""To increase / decrease The Speed of SwethAI
    [ increase by x :  +50 ]
    [ decrease by x :  -50 ]
    """)
    n = int(input("Control : "))
    engine.setProperty('rate', engine.getProperty('rate') - n)


# Hola SwethAI
def welcome():
    engine.say('Bonjour , Blesslin ')
    time.sleep(1.2)
    engine.say(' Kavya :  Roger ')
    engine.runAndWait()

# SwethAI Echo
def echo(text):
    engine.say(text)
    engine.runAndWait()


def order():
    try:
        with srec.Microphone() as me:
            print('Kavya is all ears ...')
            voice = listener.listen(me)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'kavya' in cmd:
                cmd = cmd.replace('kavya', '')
                # echo(cmd)
                pass
    except:
        pass
    return cmd


def executor():
    cmd = order()
    # print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', 'playing')
        echo(song)
        pywhatkit.playonyt(song.replace('playing', ''))


# KavyAi
welcome()

# executor()

#  TEST
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
