class Stack:
    def __init__(self, max):
        # Initialize the stack with a fixed maximum size
        self.items = [None] * max  # Create a list to hold stack elements
        self.top = -1  # The top pointer starts at -1, indicating an empty stack

    def isEmpty(self):
        # Check if the stack is empty
        return self.top == -1  # True if the top pointer is -1, False otherwise

    def push(self, item):
        # Add an element to the top of the stack
        self.top += 1  # Move the top pointer up
        self.items[self.top] = item  # Place the new item at the top position

    def pop(self):
        # Remove and return the top element of the stack
        top = self.items[self.top]  # Get the current top element
        self.items[self.top] = None  # Clear the element from the stack
        self.top -= 1  # Move the top pointer down
        return top  # Return the removed element

    def peek(self):
        # Return the top element of the stack without removing it
        if not self.isEmpty():  # Check if the stack is not empty
            return self.items[self.top]  # Return the top element

    def size(self):
        # Return the current number of elements in the stack
        return self.top + 1

    def isFull(self):
        # Check if the stack is full
        return self.top == len(self.items) - 1  # True if the top pointer equals the max

# Examples
s = Stack(10) 
s.push(10)# 10
s.push(20)# 20 10
s.push(30)# 30 20 10
s.push(40)# 40 30 20 10
s.push(50)# 50 40 30 20 10
s.pop()# 40 30 20 10
s.pop()# 30 20 10
print(s.peek())# 30
print(s.size())# 3
print(s.isEmpty())# False