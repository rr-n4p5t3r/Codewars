import java.util.Scanner;

class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;

    TreeNode(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    TreeNode root;

    TreeNode insertNode(TreeNode node, int data) {
        if (node == null) {
            return new TreeNode(data);
        }

        if (data < node.data) {
            node.left = insertNode(node.left, data);
        } else if (data > node.data) {
            node.right = insertNode(node.right, data);
        }

        return node;
    }

    boolean searchNode(TreeNode node, int data) {
        if (node == null) {
            return false;
        }

        if (node.data == data) {
            return true;
        }

        if (data < node.data) {
            return searchNode(node.left, data);
        } else {
            return searchNode(node.right, data);
        }
    }

    void inorderTraversal(TreeNode node) {
        if (node != null) {
            inorderTraversal(node.left);
            System.out.print(node.data + " ");
            inorderTraversal(node.right);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        BinaryTree binaryTree = new BinaryTree();
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("Binary Tree Options");
            System.out.println("1. Insert node");
            System.out.println("2. Search node");
            System.out.println("3. Inorder traversal");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter the value to insert: ");
                    int value = scanner.nextInt();
                    binaryTree.root = binaryTree.insertNode(binaryTree.root, value);
                    break;
                case 2:
                    System.out.print("Enter the value to search: ");
                    int searchValue = scanner.nextInt();
                    if (binaryTree.searchNode(binaryTree.root, searchValue)) {
                        System.out.println(searchValue + " found in the tree");
                    } else {
                        System.out.println(searchValue + " not found in the tree");
                    }
                    break;
                case 3:
                    System.out.println("Inorder Traversal:");
                    binaryTree.inorderTraversal(binaryTree.root);
                    System.out.println();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option");
            }

            scanner.nextLine(); // Consumir el carácter de nueva línea restante

        } while (option != 4);
    }
}
