class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_element_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_element_after_value(self, value, new_value):
        current = self.head
        while current:
            if current.data == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def add_element_before_value(self, value, new_value):
        if self.head.data == value:
            self.add_element_to_beginning(new_value)
            return
        prev = None
        current = self.head
        while current:
            if current.data == value:
                new_node = Node(new_value)
                prev.next = new_node
                new_node.next = current
                break
            prev = current
            current = current.next

    def remove_element_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def remove_element_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def remove_element(self, value):
        if self.head.data == value:
            self.remove_element_from_beginning()
            return
        prev = None
        current = self.head
        while current:
            if current.data == value:
                prev.next = current.next
                break
            prev = current
            current = current.next

    def find_element(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def clear_list(self):
        self.head = None

    def merge_lists(self, list2):
        current = self.head
        while current.next:
            current = current.next
        current.next = list2.head

    def copy_list(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.add_element_to_end(current.data)
            current = current.next
        return new_list

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("null")

if __name__ == "__main__":
    linked_list = LinkedList()
    option = 0

    while option != 14:
        print("Options")
        print("1. Add element to the end of the list")
        print("2. Add element to the beginning of the list")
        print("3. Add element after the specified value")
        print("4. Add element before the specified value")
        print("5. Remove element from the beginning of the list")
        print("6. Remove element from the end of the list")
        print("7. Remove element from the list")
        print("8. Find element in the list")
        print("9. Print the list")
        print("10. Reverse the list")
        print("11. Clear the list")
        print("12. Merge two lists")
        print("13. Copy the list")
        print("14. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            data = int(input("Enter the element to add at the end: "))
            linked_list.add_element_to_end(data)
        elif option == 2:
            data = int(input("Enter the element to add at the beginning: "))
            linked_list.add_element_to_beginning(data)
        elif option == 3:
            value = int(input("Enter the value after which to add: "))
            new_data = int(input("Enter the new element: "))
            linked_list.add_element_after_value(value, new_data)
        elif option == 4:
            value = int(input("Enter the value before which to add: "))
            new_data = int(input("Enter the new element: "))
            linked_list.add_element_before_value(value, new_data)
        elif option == 5:
            linked_list.remove_element_from_beginning()
        elif option == 6:
            linked_list.remove_element_from_end()
        elif option == 7:
            data = int(input("Enter the element to remove: "))
            linked_list.remove_element(data)
        elif option == 8:
            data = int(input("Enter the element to find: "))
            if linked_list.find_element(data):
                print(f"{data} found in the list")
            else:
                print(f"{data} not found in the list")
        elif option == 9:
            linked_list.print_list()
        elif option == 10:
            linked_list.reverse_list()
        elif option == 11:
            linked_list.clear_list()
        elif option == 12:
            list2 = LinkedList()
            elements = input("Enter elements of second list separated by spaces: ").split()
            for element in elements:
                list2.add_element_to_end(int(element))
            linked_list.merge_lists(list2)
        elif option == 13:
            copy_list = linked_list.copy_list()
            print("Copied list:")
            copy_list.print_list()
        elif option == 14:
            print("Exiting...")
        else:
            print("Invalid option")
