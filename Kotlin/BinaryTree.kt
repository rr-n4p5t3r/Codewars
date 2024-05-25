import java.util.*

class TreeNode(var data: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class BinaryTree {
    var root: TreeNode? = null

    fun insertNode(data: Int) {
        root = insertNodeRec(root, data)
    }

    private fun insertNodeRec(node: TreeNode?, data: Int): TreeNode {
        if (node == null) {
            return TreeNode(data)
        }

        if (data < node.data) {
            node.left = insertNodeRec(node.left, data)
        } else if (data > node.data) {
            node.right = insertNodeRec(node.right, data)
        }

        return node
    }

    fun searchNode(data: Int): Boolean {
        return searchNodeRec(root, data)
    }

    private fun searchNodeRec(node: TreeNode?, data: Int): Boolean {
        if (node == null) {
            return false
        }

        if (node.data == data) {
            return true
        }

        return if (data < node.data) {
            searchNodeRec(node.left, data)
        } else {
            searchNodeRec(node.right, data)
        }
    }

    fun inorderTraversal() {
        inorderTraversalRec(root)
    }

    private fun inorderTraversalRec(node: TreeNode?) {
        if (node != null) {
            inorderTraversalRec(node.left)
            print("${node.data} ")
            inorderTraversalRec(node.right)
        }
    }
}

fun main() {
    val binaryTree = BinaryTree()
    val scanner = Scanner(System.`in`)
    var option: Int

    do {
        println("Binary Tree Options")
        println("1. Insert node")
        println("2. Search node")
        println("3. Inorder traversal")
        println("4. Exit")
        print("Enter your choice: ")
        option = scanner.nextInt()

        when (option) {
            1 -> {
                print("Enter the value to insert: ")
                val value = scanner.nextInt()
                binaryTree.insertNode(value)
            }
            2 -> {
                print("Enter the value to search: ")
                val value = scanner.nextInt()
                if (binaryTree.searchNode(value)) {
                    println("$value found in the tree")
                } else {
                    println("$value not found in the tree")
                }
            }
            3 -> {
                println("Inorder Traversal:")
                binaryTree.inorderTraversal()
                println()
            }
            4 -> println("Exiting...")
            else -> println("Invalid option")
        }

        scanner.nextLine() // Consumir el carácter de nueva línea restante

    } while (option != 4)
}
