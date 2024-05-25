# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, 
# sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores 
# de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: 
# “La solución es: <solucion>”
from math import sqrt

a = float(input("digite el valor de a:"))
b = float(input("digite el valor de b:"))
c = float(input("digite el valor de c:"))

x1 = 0
x2 = 0 

if((b**2)-(4*a*c)) < 0:
    print("No se puede realizar la operacion, debido a que no se puede sacar raiz cuadrada a un numero negativo")
else:
    x1 = (-b + (sqrt((pow(b, 2)) - (4 * a * c)))) / (2 * a)
    x2 = (-b - (sqrt((pow(b, 2)) - (4 * a * c)))) / (2 * a)
    print("La solucion es: \nx1 = ", x1, "\nx2 = ", x2)
    

    

