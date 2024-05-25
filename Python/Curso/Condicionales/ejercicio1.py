# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
# Sino, decirle al usuario que no es vocal

letra = input("Digite una letra: ")

#if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es vocal")
