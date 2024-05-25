# Proyecto Aurebesh
# Desarrollado por Ricardo Rosero - n4p5t3r
# Email: rrosero2000@gmail.com

# Aqui le asigno los respectivos valores a cada una de las letras que pertenecen al idioma espanol
# por los valores de esas mismas letras en aurebesh
tabla = {'a': 'aurek', 'b': 'besh', 'c': 'cresh', 'ch':'cherek', 
         'd': 'dorn', 'e': 'esk', 'f': 'forn', 'g': 'grek', 'h': 'herf', 'i': 'isk', 
         'j': 'jenth', 'k': 'krill', 'l': 'leth', 'm': 'mern', 'n': 'nern', 'ñ': 'nen', 
         'o': 'osk', 'p': 'peth', 'q': 'qek', 'r': 'resh', 's': 'senth', 't': 'trill', 
         'u': 'usk', 'v': 'vev', 'w': 'wesk', 'x': 'xesh', 'y': 'yirt', 'z': 'zerek'}

# Pedimos al usuario que ingrese una frase en espanol
frase_espanol = input("Ingrese una frase en espanol: ")

# Convertimos la frase a minusculas
frase_espanol = frase_espanol.lower()

# Creamos una lista vacia para almacenar los caracteres traducidos
frase_aurebesh = []

# Recorremos cada caracter de la frase en espanol y lo traducimos a Aurebesh
for caracter in frase_espanol:
    if caracter in tabla:
        # Si el caracter está en la tabla de equivalencias, lo agregamos a la lista de 
        # caracteres traducidos
        frase_aurebesh.append(tabla[caracter])
    else:
        # Si el caracter no está en la tabla de equivalencias, lo dejamos como esta
        frase_aurebesh.append(caracter)

# Convertimos la lista de caracteres traducidos a una cadena
frase_aurebesh = ''.join(frase_aurebesh)

# Imprimimos la frase traducida a aurebesh
print("La frase traducida a aurebesh es: ", frase_aurebesh)
