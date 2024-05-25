# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un 
# determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
# Considere: 
# PP = ( P1 + P2 +P3 ) / 3 
# PROM = ( PP + 2*EP + 3*EF ) / 6
# Donde: P1, P2, P3 : Practicas
# PP: promedio de práctica
# PROM: promedio
# EP: examen parcial
# EF: examen final

p1 = float(input("Ingrese el valor de la practica1: "))
p2 = float(input("Ingrese el valor de la practica2: "))
p3 = float(input("Ingrese el valor de la practica3: "))
ep = float(input("Ingrese el valor del examen parcial: "))
ef = float(input("Ingrese el valor del examen final: "))

pp = (p1 + p2 + p3) / 3 
prom = (pp + (2 * ep) + (3 * ef)) / 6

print("El promedio de practica es: ", pp)
print("El promedio de general es: ", prom)
