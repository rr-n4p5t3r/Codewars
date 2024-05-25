import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    
    print("Enter the number of rows: ")
    val rows = scanner.nextInt()
    
    print("Enter the number of columns: ")
    val columns = scanner.nextInt()
    
    // Crear una matriz
    val matrix = Array(rows) { IntArray(columns) }
    
    // Asignar valores a la matriz
    for (i in 0 until rows) {
        for (j in 0 until columns) {
            print("Enter the element at position ($i, $j): ")
            matrix[i][j] = scanner.nextInt()
        }
    }
    
    // Imprimir la matriz
    println("Matrix:")
    for (i in 0 until rows) {
        for (j in 0 until columns) {
            print("${matrix[i][j]} ")
        }
        println()
    }
}
