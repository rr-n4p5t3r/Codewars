import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    private Node head;

    void addElementToEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    void addElementToBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    void addElementAfterValue(int value, int newValue) {
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                Node newNode = new Node(newValue);
                newNode.next = current.next;
                current.next = newNode;
                break;
            }
            current = current.next;
        }
    }

    void addElementBeforeValue(int value, int newValue) {
        if (head != null && head.data == value) {
            addElementToBeginning(newValue);
            return;
        }

        Node prev = null;
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                Node newNode = new Node(newValue);
                prev.next = newNode;
                newNode.next = current;
                break;
            }
            prev = current;
            current = current.next;
        }
    }

    void removeElementFromBeginning() {
        if (head != null) {
            head = head.next;
        }
    }

    void removeElementFromEnd() {
        if (head != null) {
            if (head.next == null) {
                head = null;
                return;
            }
            Node prev = null;
            Node current = head;
            while (current.next != null) {
                prev = current;
                current = current.next;
            }
            if (prev != null) {
                prev.next = null;
            }
        }
    }

    void removeElement(int value) {
        if (head != null && head.data == value) {
            removeElementFromBeginning();
            return;
        }

        Node prev = null;
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                prev.next = current.next;
                break;
            }
            prev = current;
            current = current.next;
        }
    }

    boolean findElement(int value) {
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    void reverseList() {
        Node prev = null;
        Node current = head;
        Node next;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    void clearList() {
        head = null;
    }

    void mergeLists(LinkedList list2) {
        Node current = head;
        if (current != null) {
            while (current.next != null) {
                current = current.next;
            }
            current.next = list2.head;
        } else {
            head = list2.head;
        }
    }

    LinkedList copyList() {
        LinkedList newList = new LinkedList();
        Node current = head;
        while (current != null) {
            newList.addElementToEnd(current.data);
            current = current.next;
        }
        return newList;
    }

    void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList linkedList = new LinkedList();
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("Options");
            System.out.println("1. Add element to the end of the list");
            System.out.println("2. Add element to the beginning of the list");
            System.out.println("3. Add element after the specified value");
            System.out.println("4. Add element before the specified value");
            System.out.println("5. Remove element from the beginning of the list");
            System.out.println("6. Remove element from the end of the list");
            System.out.println("7. Remove element from the list");
            System.out.println("8. Find element in the list");
            System.out.println("9. Print the list");
            System.out.println("10. Reverse the list");
            System.out.println("11. Clear the list");
            System.out.println("12. Merge two lists");
            System.out.println("13. Copy the list");
            System.out.println("14. Exit");
            System.out.print("Enter your choice: ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter the element to add at the end: ");
                    int data = scanner.nextInt();
                    linkedList.addElementToEnd(data);
                    break;
                case 2:
                    System.out.print("Enter the element to add at the beginning: ");
                    int beginningData = scanner.nextInt();
                    linkedList.addElementToBeginning(beginningData);
                    break;
                case 3:
                    System.out.print("Enter the value after which to add: ");
                    int value = scanner.nextInt();
                    System.out.print("Enter the new element: ");
                    int newData = scanner.nextInt();
                    linkedList.addElementAfterValue(value, newData);
                    break;
                case 4:
                    System.out.print("Enter the value before which to add: ");
                    int beforeValue = scanner.nextInt();
                    System.out.print("Enter the new element: ");
                    int newBeforeData = scanner.nextInt();
                    linkedList.addElementBeforeValue(beforeValue, newBeforeData);
                    break;
                case 5:
                    linkedList.removeElementFromBeginning();
                    break;
                case 6:
                    linkedList.removeElementFromEnd();
                    break;
                case 7:
                    System.out.print("Enter the element to remove: ");
                    int removeData = scanner.nextInt();
                    linkedList.removeElement(removeData);
                    break;
                case 8:
                    System.out.print("Enter the element to find: ");
                    int findData = scanner.nextInt();
                    if (linkedList.findElement(findData)) {
                        System.out.println(findData + " found in the list");
                    } else {
                        System.out.println(findData + " not found in the list");
                    }
                    break;
                case 9:
                    linkedList.printList();
                    break;
                case 10:
                    linkedList.reverseList();
                    break;
                case 11:
                    linkedList.clearList();
                    break;
                case 12:
                    LinkedList list2 = new LinkedList();
                    System.out.print("Enter elements of second list separated by spaces: ");
                    scanner.nextLine(); // Consumir el carácter de nueva línea restante
                    String input = scanner.nextLine();
                    String[] elements = input.split(" ");
                    for (String element : elements) {
                        list2.addElementToEnd(Integer.parseInt(element));
                        linkedList.mergeLists(list2);
                        break;
                    }
                case 13:
                    LinkedList copyList = linkedList.copyList();
                    System.out.println("Copied list:");
                    copyList.printList();
                    break;
                case 14:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option");
                }
                // Consumir el carácter de nueva línea restante
                scanner.nextLine();
            } while (option != 14);
        }
    }
    