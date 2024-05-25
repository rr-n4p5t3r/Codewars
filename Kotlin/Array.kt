import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    
    // Solicitar al usuario el tamaño del vector
    print("Enter the size of the array: ")
    val size = scanner.nextInt()
    
    // Crear el vector
    val array = IntArray(size)
    
    // Solicitar al usuario ingresar los elementos del vector
    println("Enter the elements of the array:")
    for (i in 0 until size) {
        print("Enter element at index $i: ")
        array[i] = scanner.nextInt()
    }
    
    // Imprimir el vector
    println("Array:")
    for (element in array) {
        print("$element ")
    }
}
