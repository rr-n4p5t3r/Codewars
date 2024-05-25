import java.util.*

class Stack {
    private val stack: MutableList<Int> = mutableListOf()

    fun push(value: Int) {
        stack.add(value)
    }

    fun pop(): Int? {
        return if (isEmpty()) {
            null
        } else {
            stack.removeAt(stack.size - 1)
        }
    }

    fun peek(): Int? {
        return if (isEmpty()) {
            null
        } else {
            stack[stack.size - 1]
        }
    }

    fun isEmpty(): Boolean {
        return stack.isEmpty()
    }

    fun printStack() {
        println(stack.joinToString(" -> "))
    }
}

fun main() {
    val stack = Stack()
    val scanner = Scanner(System.`in`)
    var option: Int

    do {
        println("Stack Options")
        println("1. Push element")
        println("2. Pop element")
        println("3. Peek element")
        println("4. Print stack")
        println("5. Exit")
        print("Enter your choice: ")
        option = scanner.nextInt()

        when (option) {
            1 -> {
                print("Enter the element to push: ")
                val element = scanner.nextInt()
                stack.push(element)
            }
            2 -> {
                val poppedElement = stack.pop()
                if (poppedElement != null) {
                    println("Popped element: $poppedElement")
                } else {
                    println("Stack is empty, cannot pop element.")
                }
            }
            3 -> {
                val topElement = stack.peek()
                if (topElement != null) {
                    println("Top element: $topElement")
                } else {
                    println("Stack is empty, cannot peek element.")
                }
            }
            4 -> {
                println("Current stack:")
                stack.printStack()
            }
            5 -> println("Exiting...")
            else -> println("Invalid option")
        }

        scanner.nextLine() // Consumir el carácter de nueva línea restante

    } while (option != 5)
}
