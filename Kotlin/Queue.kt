import java.util.*

class Queue {
    private val queue: Queue<Int> = LinkedList()

    fun enqueue(value: Int) {
        queue.add(value)
    }

    fun dequeue(): Int? {
        return if (isEmpty()) {
            null
        } else {
            queue.remove()
        }
    }

    fun peek(): Int? {
        return if (isEmpty()) {
            null
        } else {
            queue.peek()
        }
    }

    fun isEmpty(): Boolean {
        return queue.isEmpty()
    }

    fun printQueue() {
        println(queue.joinToString(" -> "))
    }
}

fun main() {
    val queue = Queue()
    val scanner = Scanner(System.`in`)
    var option: Int

    do {
        println("Queue Options")
        println("1. Enqueue element")
        println("2. Dequeue element")
        println("3. Peek element")
        println("4. Print queue")
        println("5. Exit")
        print("Enter your choice: ")
        option = scanner.nextInt()

        when (option) {
            1 -> {
                print("Enter the element to enqueue: ")
                val element = scanner.nextInt()
                queue.enqueue(element)
            }
            2 -> {
                val dequeuedElement = queue.dequeue()
                if (dequeuedElement != null) {
                    println("Dequeued element: $dequeuedElement")
                } else {
                    println("Queue is empty, cannot dequeue element.")
                }
            }
            3 -> {
                val frontElement = queue.peek()
                if (frontElement != null) {
                    println("Front element: $frontElement")
                } else {
                    println("Queue is empty, cannot peek element.")
                }
            }
            4 -> {
                println("Current queue:")
                queue.printQueue()
            }
            5 -> println("Exiting...")
            else -> println("Invalid option")
        }

        scanner.nextLine() // Consumir el carácter de nueva línea restante

    } while (option != 5)
}
