class Node:
    def __init__(self, data=None, next=None, prv=None):
        # Initialize a node with data, next pointer, and previous pointer
        self.data = data  # Data stored in the node
        self.next = next  # Pointer to the next node
        self.previous = prv  # Pointer to the previous node

    def setData(self, newData):
        # Set new data for the node
        self.data = newData

    def getData(self):
        # Get the data from the node
        return self.data

    def setNext(self, newNext):
        # Set the pointer to the next node
        self.next = newNext

    def getNext(self):
        # Get the pointer to the next node
        return self.next

    def hasNext(self):
        # Check if the node has a next node
        return self.next != None

    def setPrevious(self, newprv):
        # Set the pointer to the previous node
        self.previous = newprv

    def getPrevious(self):
        # Get the pointer to the previous node
        return self.previous

    def hasPrevious(self):
        # Check if the node has a previous node
        return self.previous != None


class DoubleyLinkedList:
    def __init__(self):
        # Initialize a doubly linked list with head and tail
        self.head = None  # Head pointer
        self.tail = None  # Tail pointer

    def addAtBeginning(self, item):
        # Add a new node at the beginning of the list
        newnode = Node(item)  # Create a new node
        if self.head == None:  # If the list is empty
            self.head = self.tail = newnode  # Set head and tail to the new node
        else:
            newnode.setPrevious(None)  # Set the previous of the new node to None
            newnode.setNext(self.head)  # Set the next of the new node to the current head
            self.head.setPrevious(newnode)  # Update the previous of the current head
            self.head = newnode  # Update the head to the new node

    def addAtEnd(self, item):
        # Add a new node at the end of the list
        newnode = Node(item)  # Create a new node
        if self.head == None:  # If the list is empty
            self.head = self.tail = newnode  # Set head and tail to the new node
        self.tail.setNext(newnode)  # Set the next of the current tail to the new node
        newnode.setPrevious(self.tail)  # Set the previous of the new node to the current tail
        self.tail = newnode  # Update the tail to the new node

    def addAtPosition(self, item, pos):
        # Add a new node at a specific position
        if pos < 0:  # Check for invalid position
            return None
        newnode = Node(item)  # Create a new node
        count = 0
        cur = self.head  # Start from the head
        while count < pos - 1:  # Traverse to the node before the position
            count += 1
            cur = cur.getNext()
        newnode.setNext(cur.getNext())  # Set the next of the new node
        newnode.setPrevious(cur)  # Set the previous of the new node
        cur.getNext().setPrevious(newnode)  # Update the previous of the next node
        cur.setNext(newnode)  # Update the next of the current node

    def Remove(self, item):
        # Remove a node with a specific value
        cur = self.head  # Start from the head
        found = 0  # Flag to indicate if the item is found
        while found == 0:  # Traverse until the item is found
            if cur.getData() == item:  # Check if the current node's data matches
                found = 1
            else:
                cur = cur.getNext()
        if cur.getPrevious() == None:  # If the item is at the head
            self.head = cur.getNext()  # Update the head to the next node
        else:
            cur.getPrevious().setNext(cur.getNext())  # Update the previous node's next pointer
            cur.getNext().setPrevious(cur.getPrevious())  # Update the next node's previous pointer

    def printlist(self):
        # Print all elements of the list
        cur = self.head  # Start from the head
        while cur:  # Traverse the list
            print(cur.getData(), end=" -> ")  # Print the data of the current node
            cur = cur.getNext()  # Move to the next node
        print("None")  # End of the list


# Example usage
D = DoubleyLinkedList()  # Create a doubly linked list
D.addAtBeginning(10)  # Add 10 at the beginning
D.addAtEnd(30)  # Add 30 at the end
D.addAtPosition(20, 1)  # Add 20 at position 1
D.addAtEnd(40)  # Add 40 at the end
D.addAtEnd(50)  # Add 50 at the end
D.addAtBeginning(0)  # Add 0 at the beginning
D.printlist()  # Print the list: 0 -> 10 -> 20 -> 30 -> 40 -> 50 -> None
D.Remove(30)  # Remove the node with value 30
D.printlist()  # Print the list: 0 -> 10 -> 20 -> 40 -> 50 -> None