class Queue:
    def __init__(self, size):
        # Initialize the queue with a fixed size
        self.maxsize = size  # Maximum size of the queue
        self.items = [None] * size  # List to store queue elements
        self.front = 0  # Pointer to the front of the queue
        self.rear = self.maxsize - 1  # Pointer to the rear of the queue
        self.nitems = 0  # Number of items currently in the queue

    def isFull(self):
        # Check if the queue is full
        return self.nitems == self.maxsize

    def isEmpty(self):
        # Check if the queue is empty
        return self.nitems == 0

    def QueueLength(self):
        # Return the current length of the queue
        return self.nitems

    def Enqueue(self, item):
        # Add an element to the rear of the circular queue
        if self.isFull():  # Check for overflow
            raise Exception("Queue OverFlow")
        self.rear = (self.rear + 1) % self.maxsize  # Update rear pointer circularly
        self.items[self.rear] = item  # Add the item to the queue
        self.nitems += 1  # Increment the count of items

    def Dequeue(self):
        # Remove an element from the front of the circular queue
        if self.isEmpty():  # Check for underflow
            raise Exception("Queue UnderFlow")
        frontitem = self.items[self.front]  # Get the front element
        self.items[self.front] = None  # Remove the front element
        self.front = (self.front + 1) % self.maxsize  # Update front pointer circularly
        self.nitems -= 1  # Decrement the count of items
        return frontitem  # Return the removed element

    def peek(self):
        # Return the front element without removing it
        if self.isEmpty():  # Check if the queue is empty
            return None  # Return None if the queue is empty
        else:
            return self.items[self.front]  # Return the front element

# Examples
Q = Queue(5)  # Create a queue with a size of 5
Q.Enqueue(10)  # Add 10 to the queue
Q.Enqueue(20)  # Add 20 to the queue
Q.Enqueue(30)  # Add 30 to the queue
Q.Enqueue(40)  # Add 40 to the queue
print(Q.Dequeue())  # Remove and print the front element (10)
print(Q.peek())  # Print the front element (20) without removing it