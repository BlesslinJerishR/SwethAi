# importers
import time
import speech_recognition as srec
import pyttsx3
import pywhatkit
import datetime

# SETTINGS

# Bot Profile
BOT = "Nazeer"
# Alias [ Optional ]
# TODO: Alias BUG
BOTS = ["dei",
        "day",
        "naseer",
        "nazeer",
        "nazer",
        "nazir",
        "nasir"]

# Audio Engine
engine = pyttsx3.init()

# Default SwethAI Voice
engine.setProperty('voice', engine.getProperty('voices')[0].id)

# Default SwethAI Speed
engine.setProperty('rate', engine.getProperty('rate') - 50)

# [x] TODO : Summon Flags
summon = False


def someone_true():
    global summon
    summon = True
    print("I am someone")


# Server Listener
def server():
    try:
        print(f'{BOT} is all ears ...')
        listener = srec.Recognizer()
        listener.pause_threshold = 1
        with srec.Microphone() as me:
            voice = listener.listen(me)
            cmd = listener.recognize_google(voice)
            listener.adjust_for_ambient_noise(me)
            cmd = cmd.lower()
            cmd = cmd.replace(BOT, '')
            print(cmd)
            for x in BOTS:
                if x in cmd:
                    someone_true()
                    break
    except Exception as e:
        if ValueError:
            print(e)
            echo("Chetha Payaley")
            engine.runAndWait()
    return cmd


# Voice Changer
# You can't change your Girlfriend's attitude at least change her gender
def voice_changer(n):
    print(f"""To Change The Vocal Cord of SwethAI
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
    engine.setProperty('rate', int(engine.getProperty('rate')) - n)


# Hola SwethAI
def welcome():
    engine.say('Bonjour , Blesslin Jerish')
    time.sleep(1)
    engine.say(f'{BOT} , on your marks')
    # Summoning FBOT
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say('Aye lieutenant  , Roger ')
    engine.runAndWait()


# SwethAI Echo
def echo(text):
    # test ^ 1
    print(text)
    engine.say(text)
    engine.runAndWait()


# Executor Skeleton
def torder():
    """
    Just a skeleton for Logical Orders
    :return: command script
    """
    # print(cmd)
    coms = "#Logic"
    if 'command' in coms:
        song = coms.replace('command', 'commanding')
        echo(song)
        pywhatkit.playonyt(song.replace('commanding', ''))
    return coms


# To play songs on YouTube
def youtuber(cmd):
    # cmd = order()
    songer = cmd.replace('play', 'playing')
    echo(songer)
    song = songer.replace('playing', '')
    pywhatkit.playonyt(song)
    engine.runAndWait()


# To Tell the Clock
def timez():
    t = datetime.datetime.now().strftime("%H:%M")
    echo(f"The Time is {t} ")


# By The Order of FBOT
def orders():
    cmd = server()
    if summon:
        if 'play' in cmd:
            youtuber(cmd)
        elif 'time' in cmd:
            timez()
    else:
        echo("There is someone in here with us")
    # Logic has Left The chat


# Firing the FBOT
# welcome()
origin = True
while origin:
    orders()
