import java.util.Scanner

class Node(var data: Int) {
    var next: Node? = null
}

class LinkedList {
    private var head: Node? = null

    fun addElementToEnd(data: Int) {
        val newNode = Node(data)
        if (head == null) {
            head = newNode
        } else {
            var current = head
            while (current?.next != null) {
                current = current.next
            }
            current?.next = newNode
        }
    }

    fun addElementToBeginning(data: Int) {
        val newNode = Node(data)
        newNode.next = head
        head = newNode
    }

    fun addElementAfterValue(value: Int, newValue: Int) {
        var current = head
        while (current != null) {
            if (current.data == value) {
                val newNode = Node(newValue)
                newNode.next = current.next
                current.next = newNode
                break
            }
            current = current.next
        }
    }

    fun addElementBeforeValue(value: Int, newValue: Int) {
        if (head?.data == value) {
            addElementToBeginning(newValue)
            return
        }

        var prev: Node? = null
        var current = head
        while (current != null) {
            if (current.data == value) {
                val newNode = Node(newValue)
                prev?.next = newNode
                newNode.next = current
                break
            }
            prev = current
            current = current.next
        }
    }

    fun removeElementFromBeginning() {
        head = head?.next
    }

    fun removeElementFromEnd() {
        if (head?.next == null) {
            head = null
            return
        }
        var prev: Node? = null
        var current = head
        while (current?.next != null) {
            prev = current
            current = current.next
        }
        prev?.next = null
    }

    fun removeElement(value: Int) {
        if (head?.data == value) {
            removeElementFromBeginning()
            return
        }

        var prev: Node? = null
        var current = head
        while (current != null) {
            if (current.data == value) {
                prev?.next = current.next
                break
            }
            prev = current
            current = current.next
        }
    }

    fun findElement(value: Int): Boolean {
        var current = head
        while (current != null) {
            if (current.data == value) {
                return true
            }
            current = current.next
        }
        return false
    }

    fun reverseList() {
        var prev: Node? = null
        var current = head
        var next: Node?
        while (current != null) {
            next = current.next
            current.next = prev
            prev = current
            current = next
        }
        head = prev
    }

    fun clearList() {
        head = null
    }

    fun mergeLists(list2: LinkedList) {
        var current = head
        while (current?.next != null) {
            current = current.next
        }
        current?.next = list2.head
    }

    fun copyList(): LinkedList {
        val newList = LinkedList()
        var current = head
        while (current != null) {
            newList.addElementToEnd(current.data)
            current = current.next
        }
        return newList
    }

    fun printList() {
        var current = head
        while (current != null) {
            print("${current.data} -> ")
            current = current.next
        }
        println("null")
    }
}

fun main() {
    val linkedList = LinkedList()
    val scanner = Scanner(System.`in`)
    var option: Int

    do {
        println("Options")
        println("1. Add element to the end of the list")
        println("2. Add element to the beginning of the list")
        println("3. Add element after the specified value")
        println("4. Add element before the specified value")
        println("5. Remove element from the beginning of the list")
        println("6. Remove element from the end of the list")
        println("7. Remove element from the list")
        println("8. Find element in the list")
        println("9. Print the list")
        println("10. Reverse the list")
        println("11. Clear the list")
        println("12. Merge two lists")
        println("13. Copy the list")
        println("14. Exit")
        print("Enter your choice: ")
        option = scanner.nextInt()

        when (option) {
            1 -> {
                print("Enter the element to add at the end: ")
                val data = scanner.nextInt()
                linkedList.addElementToEnd(data)
            }
            2 -> {
                print("Enter the element to add at the beginning: ")
                val data = scanner.nextInt()
                linkedList.addElementToBeginning(data)
            }
            3 -> {
                print("Enter the value after which to add: ")
                val value = scanner.nextInt()
                print("Enter the new element: ")
                val newData = scanner.nextInt()
                linkedList.addElementAfterValue(value, newData)
            }
            4 -> {
                print("Enter the value before which to add: ")
                val value = scanner.nextInt()
                print("Enter the new element: ")
                val newData = scanner.nextInt()
                linkedList.addElementBeforeValue(value, newData)
            }
            5 -> linkedList.removeElementFromBeginning()
            6 -> linkedList.removeElementFromEnd()
            7 -> {
                print("Enter the element to remove: ")
                val data = scanner.nextInt()
                linkedList.removeElement(data)
            }
            8 -> {
                print("Enter the element to find: ")
                val data = scanner.nextInt()
                if (linkedList.findElement(data)) {
                    println("$data found in the list")
                } else {
                    println("$data not found in the list")
                }
            }
            9 -> linkedList.printList()
            10 -> linkedList.reverseList()
            11 -> linkedList.clearList()
            12 -> {
                val list2 = LinkedList()
                print("Enter elements of second list separated by spaces: ")
                val elements = readLine()!!.split(" ").map { it.toInt() }
                elements.forEach { list2.addElementToEnd(it) }
                linkedList.mergeLists(list2)
            }
            13 -> {
                val copyList = linkedList.copyList()
                println("Copied list:")
                copyList.printList()
            }
            14 -> println("Exiting...")
            else -> println("Invalid option")
        }
        // Consumir el carácter de nueva línea restante
        scanner.nextLine()
    } while (option != 14)
}
