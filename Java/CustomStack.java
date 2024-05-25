import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class CustomStack {
    private List<Integer> stack;

    public CustomStack() {
        stack = new ArrayList<>();
    }

    public void push(int value) {
        stack.add(value);
    }

    public Integer pop() {
        return stack.isEmpty() ? null : stack.remove(stack.size() - 1);
    }

    public Integer peek() {
        return stack.isEmpty() ? null : stack.get(stack.size() - 1);
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }

    public void printStack() {
        System.out.println(stack.toString().replaceAll("[\\[\\],]", " -> "));
    }
}

public class Main {
    public static void main(String[] args) {
        CustomStack stack = new CustomStack();
        Scanner scanner = new Scanner(System.in);
        int option;

        do {
            System.out.println("Stack Options");
            System.out.println("1. Push element");
            System.out.println("2. Pop element");
            System.out.println("3. Peek element");
            System.out.println("4. Print stack");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter the element to push: ");
                    int element = scanner.nextInt();
                    stack.push(element);
                    break;
                case 2:
                    Integer poppedElement = stack.pop();
                    if (poppedElement != null) {
                        System.out.println("Popped element: " + poppedElement);
                    } else {
                        System.out.println("Stack is empty, cannot pop element.");
                    }
                    break;
                case 3:
                    Integer topElement = stack.peek();
                    if (topElement != null) {
                        System.out.println("Top element: " + topElement);
                    } else {
                        System.out.println("Stack is empty, cannot peek element.");
                    }
                    break;
                case 4:
                    System.out.println("Current stack:");
                    stack.printStack();
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
