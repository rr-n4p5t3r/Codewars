import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class CustomQueue {
    private Queue<Integer> queue;

    public CustomQueue() {
        queue = new LinkedList<>();
    }

    public void enqueue(int value) {
        queue.add(value);
    }

    public Integer dequeue() {
        return queue.isEmpty() ? null : queue.remove();
    }

    public Integer peek() {
        return queue.isEmpty() ? null : queue.peek();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public void printQueue() {
        System.out.println(queue.toString().replaceAll("[\\[\\],]", " -> "));
    }
}

public class Main {
    public static void main(String[] args) {
        CustomQueue queue = new CustomQueue();
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("Queue Options");
            System.out.println("1. Enqueue element");
            System.out.println("2. Dequeue element");
            System.out.println("3. Peek element");
            System.out.println("4. Print queue");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter the element to enqueue: ");
                    int element = scanner.nextInt();
                    queue.enqueue(element);
                    break;
                case 2:
                    Integer dequeuedElement = queue.dequeue();
                    if (dequeuedElement != null) {
                        System.out.println("Dequeued element: " + dequeuedElement);
                    } else {
                        System.out.println("Queue is empty, cannot dequeue element.");
                    }
                    break;
                case 3:
                    Integer frontElement = queue.peek();
                    if (frontElement != null) {
                        System.out.println("Front element: " + frontElement);
                    } else {
                        System.out.println("Queue is empty, cannot peek element.");
                    }
                    break;
                case 4:
                    System.out.println("Current queue:");
                    queue.printQueue();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option");
            }

            scanner.nextLine(); // Consumir el carácter de nueva línea restante

        } while (option != 5);

        scanner.close();
    }
}
