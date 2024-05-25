nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))

if nombre == "Juan":
    if edad >= 18:
        print("Eres Juan y tienes mayoria de edad")
    else:
        print("Eres Juan pero no tienes mayoria de edad")
else:
    print("No eres Juan")