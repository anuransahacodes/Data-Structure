class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Manages the linked list operations (insert, display, search)."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Inserts a new node at the head of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        # Link the last node to the new node
        temp.next = new_node

    def display(self):
        """Prints the entire list content."""
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(output) + " -> None")

    # --- TASK: Add Search Functionality ---
    def search(self, key):
        """
        Traverses the list to find a node containing the specified 'key'.
        Returns True if found, False otherwise.
        """
        current = self.head  # Start from the head of the list

        # Loop until 'current' becomes None (end of list)
        while current:
            # Check if the current node's data matches the key
            if current.data == key:
                print(f"Search result: Found '{key}' in the list.")
                return True
            
            # Move to the next node
            current = current.next

        # If the loop finishes without finding the key
        print(f"Search result: '{key}' Not Found in the list.")
        return False

# Example usage to test all functionalities:
ll = LinkedList()
ll.insert_at_beginning(10) # List: 10 -> None
ll.insert_at_beginning(20) # List: 20 -> 10 -> None
ll.insert_at_end(30)       # List: 20 -> 10 -> 30 -> None
ll.insert_at_end(40)       # List: 20 -> 10 -> 30 -> 40 -> None

print("Current List:")
ll.display()

# Testing the new search function
ll.search(30) # Expected: Found (True)
ll.search(20) # Expected: Found (True)
ll.search(55) # Expected: Not Found (False)