class Node:
    """Represents a single node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Manages the circular linked list operations."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Inserts a new node at the end of the circular list."""
        new_node = Node(data)
        
        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Points back to itself
            return
            
        # Case 2: List is not empty, find the last node
        temp = self.head
        # Traverse until we reach the node whose 'next' is the head
        while temp.next != self.head:
            temp = temp.next
        
        # 1. New node links back to the head (completes the circle)
        new_node.next = self.head
        # 2. Last node's 'next' links to the new node
        temp.next = new_node

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the circular list."""
        new_node = Node(data)
        
        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
            
        # Case 2: List is not empty
        temp = self.head
        # Traverse to the last node
        while temp.next != self.head:
            temp = temp.next
            
        # 1. New node links to the current head
        new_node.next = self.head
        # 2. The last node links to the new node
        temp.next = new_node
        # 3. Head is moved to the new node
        self.head = new_node

    def display(self):
        """Prints the entire list content, showing the circular link."""
        if self.head is None:
            print("List is empty")
            return
            
        temp = self.head
        output = []
        while True:
            output.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        
        print(" -> ".join(output) + " -> (back to " + str(self.head.data) + ")")

# Example usage from the document:
cll = CircularLinkedList()

print("1. Building the list...")
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
print("Original list:")
cll.display()

cll.insert_at_beginning(5)
print("\n2. After inserting 5 at beginning:")
cll.display()

cll.insert_at_end(40)
print("\n3. After inserting 40 at end:")
cll.display()