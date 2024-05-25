# Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
# El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser 
# concatenadas ambas
minuscula = input("Digite una vocal en minuscula: ") 
mayuscula = input("Digite una vocal en mayuscula: ")

toMinuscula = (mayuscula.lower())
toMayuscula = (minuscula.upper()) 

print("Vocales {} / {} ".format(minuscula, mayuscula), "concatenadas y convertidas: {}{}".format(toMayuscula, toMinuscula))
