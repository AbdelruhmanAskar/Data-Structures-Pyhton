class Node(object):
    def __init__(self, datum):
        # Initialize a node with data and a pointer to the next node
        self.data = datum  # Data stored in the node
        self.next = None  # Pointer to the next node, initially set to None

    def getData(self):
        # Return the data stored in the node
        return self.data

    def setData(self, newdata):
        # Update the data stored in the node
        self.data = newdata

    def getNext(self):
        # Return the next node
        return self.next

    def setNext(self, newnext):
        # Update the pointer to the next node
        self.next = newnext


class Unorderedlist:
    def __init__(self):
        # Initialize an unordered list with no head node
        self.head = None  # The head of the list, initially set to None

    def isEmpty(self):
        # Check if the list is empty
        return self.head == None

    def addfirst(self, item):
        # Add an item to the beginning of the list
        temp = Node(item)  # Create a new node with the given item
        temp.setNext(self.head)  # Set the new node's next to the current head
        self.head = temp  # Update the head to the new node

    def size(self):
        # Return the number of items in the list
        cur = self.head  # Start from the head
        count = 0  # Initialize count
        while cur != None:  # Traverse the list
            count += 1  # Increment count for each node
            cur = cur.getNext()  # Move to the next node
        return count

    def Search(self, item):
        # Search for an item in the list
        cur = self.head  # Start from the head
        Found = 0  # Flag to indicate if the item is found
        while cur != None and Found == 0:  # Traverse the list until found or end
            if cur.getData() == item:  # Check if the current node's data matches
                Found = 1  # Set the flag to indicate the item is found
            else:
                cur = cur.getNext()  # Move to the next node
        return Found

    def Remove(self, item):
        # Remove an item from the list
        cur = self.head  # Start from the head
        prv = None  # Previous node, initially set to None
        Found = 0  # Flag to indicate if the item is found
        while Found == 0:  # Traverse the list until the item is found
            if cur.getData() == item:  # Check if the current node's data matches
                Found = 1  # Set the flag to indicate the item is found
                break
            else:
                prv = cur  # Update previous node
                cur = cur.getNext()  # Move to the next node
        if prv == None:  # If the item is at the head of the list
            self.head = cur.getNext()  # Update the head to the next node
        else:
            prv.setNext(cur.getNext())  # Update the previous node's next pointer


# Example usage
l = Unorderedlist()  # Create a new unordered list
l.addfirst(40)  # Add 40 to the beginning of the list
l.addfirst(30)  # Add 30 to the beginning of the list
l.addfirst(20)  # Add 20 to the beginning of the list
l.addfirst(10)  # Add 10 to the beginning of the list
print(l.size())  # Print the size of the list (4)
print(l.Search(30))  # Search for 30 in the list (1 if found, 0 otherwise)
l.Remove(20)  # Remove 20 from the list
print(l.size())  # Print the size of the list after removal (3)
