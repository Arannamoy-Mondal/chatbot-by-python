import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alpha= pyttsx3.init()
voices = alpha.getProperty('voices')
alpha.setProperty('voice', voices[1].id)


def talk(text):
    alpha.say(text)
    alpha.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alpha' in command:
                command = command.replace('alpha', '')
    except:
        pass
    return command


def run_alpha():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    # elif 'joke' in command:
    #     talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_alpha()