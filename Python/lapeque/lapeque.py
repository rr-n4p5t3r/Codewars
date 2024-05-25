import speech_recognition as sr
import pyttsx3
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import spacy

# nlp = spacy.load('es_core_news_sm')
# doc = nlp('Hola, ¿cómo estás?')

# for token in doc:
#    print(token.text)

# Predefined responses
responses = [
    "Hello, how are you?",
    "My name is La Peque.",
    "I'm an AI system under development.",
    "The current date is: {current_date}",
    "I'm fine, thanks.",
    "The current time is: {current_time}"
]

# Training data
X_train = [
    "hello",
    "what is your name?",
    "who are you?",
    "date please",
    "how are you?",
    "time please"
]
y_train = [0, 1, 2, 3, 4, 5]

# Vectorize training data
vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)

# Train classifier
clf = MultinomialNB()
clf.fit(X_train_vectors, y_train)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You say: {text}")
        return text
    except:
        print("Sorry I didn't understand you.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    
    # Set voice properties
    voices = engine.getProperty('voices')
    for voice in voices:
        if "spanish" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
        elif "english" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    engine.say(text)
    engine.runAndWait()

def respond(text):
    # Vectorize input text
    text_vector = vectorizer.transform([text])
    # Predict response index
    response_index = clf.predict(text_vector)[0]
    # Get response text and format if necessary
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    response_text=responses[response_index].format(current_time=current_time)
     
    # Speak response
    speak(response_text)
    engine = pyttsx3.init()
    
    
    '''
    if "Hola Peque" in text.lower():
        text = text.lower().replace("Hola", "")
        if "hola" in text.lower():
            speak("Hola! En qué puedo ayudarte?")
        elif "cuál es tu nombre?" in text:
            speak("Hola soy La Peque, un sistema de inteligencia artificial. Actualmente me encuentro en fase de desarrollo por parte de RR Soluciones IT.")
        elif "qué hora es?" in text:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            speak(f"La hora actual es: {current_time}")
        else:
            speak("Lo siento no te entendí.")
    '''

while True:
    text = listen()
    respond(text)