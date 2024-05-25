import random
import string
import nltk
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Descargar las herramientas necesarias para procesamiento del lenguaje natural (nltk)
nltk.download('punkt')
nltk.download('wordnet')

# Definir las respuestas del asistente
saludos = ['hola', 'hey', 'buenos días', 'buenas tardes', 'buenas noches']
despedidas = ['adiós', 'hasta luego', 'chao', 'nos vemos']
frases_aleatorias = ['No entiendo lo que estás diciendo.', 'Podrías repetir eso, por favor?', 'No estoy seguro de lo que quieres decir.']

# Definir la función para generar una respuesta
def generar_respuesta(usuario_input):
    respuesta = ''
    
    # Agregar la entrada del usuario al corpus
    corpus.append(usuario_input)
    
    # Calcular la matriz tf-idf del corpus
    tfidf_vectorizer = TfidfVectorizer(tokenizer=lemmatize_tokens)
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    
    # Calcular la similitud coseno entre la entrada del usuario y el corpus
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    index = similarities.argmax()
    
    # Generar una respuesta adecuada o una respuesta aleatoria si no se puede determinar una respuesta adecuada
    if similarities[index] < 0.2:
        respuesta = random.choice(frases_aleatorias)
    else:
        respuesta = corpus[index]
        
    return respuesta

# Definir la función para lematizar los tokens
def lemmatize_tokens(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalnum()]

# Inicializar el corpus con algunas respuestas predefinidas
corpus = ['Hola, ¿en qué puedo ayudarte?', '¿Cómo estás?', '¿Qué planes tienes para hoy?']

# Pedir al usuario que introduzca su nombre
nombre = input('¿Cómo te llamas? ')

# Saludar al usuario
saludo = random.choice(saludos)
print(saludo + ', ' + nombre + '!')

# Iniciar el bucle principal del asistente
while True:
    # Pedir al usuario que introduzca una entrada
    usuario_input = input('> ').lower()
    
    # Detectar si el usuario quiere terminar la conversación
    if usuario_input in despedidas:
        despedida = random.choice(despedidas)
        print(despedida + ', ' + nombre + '. ¡Que tengas un buen día!')
        break
    
    # Generar una respuesta y mostrarla en pantalla
    respuesta = generar_respuesta(usuario_input)
    print(respuesta)
