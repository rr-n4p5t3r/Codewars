import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar al usuario el tamaño del vector
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Crear el vector
        int[] array = new int[size];

        // Solicitar al usuario ingresar los elementos del vector
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            System.out.print("Enter element at index " + i + ": ");
            array[i] = scanner.nextInt();
        }

        // Imprimir el vector
        System.out.println("Array:");
        for (int element : array) {
            System.out.print(element + " ");
        }
    }
}
