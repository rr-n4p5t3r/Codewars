import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Configurar el reconocimiento de voz y la síntesis de voz
listener = sr.Recognizer()
engine = pyttsx3.init()

# Definir la función para hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Definir la función para escuchar
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-US')
            command = command.lower()
            if 'asistant' in command:
                command = command.replace('asistant', '')
                print(command)
    except:
        pass
    return command

# Función principal
def run():
    command = listen()
    if 'time' in command:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + hora)
    elif 'wikipedia' in command:
        command = command.replace('wikipedia', '')
        info = wikipedia.summary(command, 1)
        talk(info)
    else:
        talk('Im sorry, I dont understand you.')

while True:
    run()
