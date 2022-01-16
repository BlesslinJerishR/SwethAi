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
engine.setProperty('rate', engine.getProperty('rate') - 60)


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
    engine.say('Commander , Blesslin Jerish')
    time.sleep(1)
    engine.say('Kavya , on your marks')
    # Summoning Kavya
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say('Aye lieutenant  ; Roger ')
    engine.runAndWait()


# SwethAI Echo
def echo(text):
    engine.say(text)
    engine.runAndWait()
    # test ^ 1
    print(text)

# Executor Skeleton
def executor():
    cmd = order()
    # print(cmd)
    if 'command' in cmd:
        song = cmd.replace('command', 'commanding')
        echo(song)
        pywhatkit.playonyt(song.replace('commanding', ''))
    return cmd


# By The Order of Kavya
def order():
    with srec.Microphone() as me:
        print('Kavya is all ears ...')
        voice = listener.listen(me)
        cmd = listener.recognize_google(voice)
        cmd = cmd.lower()
        if 'kavya' and 'play' in cmd:
            cmd = cmd.replace('kavya', '')
            youtuber(cmd)
            engine.runAndWait()
            # Logical orders
        else:
            echo("Poda Panni")
            engine.runAndWait()
    return cmd


# To play songs on YouTube
def youtuber(cmd):
    # cmd = order()
    songer = cmd.replace('play', 'playing')
    echo(songer)
    song = songer.replace('playing', '')
    pywhatkit.playonyt(song)
    engine.runAndWait()


# Fire @ KavyAi
welcome()
origin = True
while origin:
    order()

# executor()
