import java.util.*

class Graph(private val vertices: Int) {
    private val adjacencyMatrix: Array<IntArray> = Array(vertices) { IntArray(vertices) }

    init {
        for (i in 0 until vertices) {
            for (j in 0 until vertices) {
                adjacencyMatrix[i][j] = 0
            }
        }
    }

    fun addEdge(src: Int, dest: Int) {
        adjacencyMatrix[src][dest] = 1
        adjacencyMatrix[dest][src] = 1
    }

    fun printGraph() {
        println("Adjacency Matrix:")
        for (i in 0 until vertices) {
            for (j in 0 until vertices) {
                print("${adjacencyMatrix[i][j]} ")
            }
            println()
        }
    }
}

fun main() {
    val scanner = Scanner(System.`in`)
    print("Enter the number of vertices: ")
    val vertices = scanner.nextInt()

    val graph = Graph(vertices)
    var option: Int

    do {
        println("Graph Options")
        println("1. Add edge")
        println("2. Print graph")
        println("3. Exit")
        print("Enter your choice: ")
        option = scanner.nextInt()

        when (option) {
            1 -> {
                print("Enter source vertex: ")
                val src = scanner.nextInt()
                print("Enter destination vertex: ")
                val dest = scanner.nextInt()
                graph.addEdge(src, dest)
            }
            2 -> {
                graph.printGraph()
            }
            3 -> println("Exiting...")
            else -> println("Invalid option")
        }

    } while (option != 3)
}
