// Swift

import Foundation

// Hola Mundo
/*
 Este es un comentario
*/
print("Hola mundo")

// Variables
var myString = "Esto es una cadena de texto"
myString = "Cambio el valor de myString"
print(myString)

var myString2: String = "Esto es otra cadena de texto"
print(myString2)

var myInt = 6
myInt = myInt + 4
print(myInt)
print(myInt - 1)
print(myInt * 2)

var myInt2 = 5
print(myInt2)

var myDouble = 6.5
print(myDouble)

var myFloat: Float = 5.6
print(myFloat)

var myBool = false
myBool = true
print(myBool)

// Constantes 
let myConst = "Esto es una constante"
print(myConst)

// Control de flujo
if myInt == 10 {
    print("El valor es 10")
}
else {
    print("El valor no es 10")
}

// Opcionales
var myOptional: String? = "Esto es un opcional"
myOptional = nil
if myOptional != nil{
    print(myOptional)
}

// Listas - imprimen en orden
var myList = ["Objeto1", "Objeto2", "Objeto3"]
print(myList)
print(myList[0])
myList.append("Objeto4")
print(myList)

// Sets - no imprimen en orden
var mySet: Set = ["Set1", "Set2", "Set3"]
print(mySet)

// Mapas
var myMap = ["Map1":1, "Map2":2]
print(myMap)
if let valor = myMap["Map3"]{
    print(age)
}
else{
    print("No existe la llave")
}

// Bucle
for value in myList{
    print(value)
}

var index = 0

while index < myList.count {
    print(myList[index])
    index += 1
}

// Funciones
func myFunction(){
    print("Esto es una funcion")
}
(0...50).forEach{
    _ in
    myFunction()
}

// Clases
class MyClass {
    var name: String?
    var age: Int?    
}
var myClass = MyClass()
myClass.name = "n4p5t3r"
myClass.age = 42