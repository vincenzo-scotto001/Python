"""
This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap

"""

import heapq

class Stack:
    def __init__(self):
        self.heap = []
        self.timestamp = 0

    def push(self, item):
        # Increment the timestamp
        self.timestamp += 1
        
        # Push a tuple of (negative timestamp, item) onto the heap
        # We use negative timestamp because heapq implements a min heap,
        # but we want the most recent (highest timestamp) item to be on top
        heapq.heappush(self.heap, (-self.timestamp, item))

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty stack")
        
        # Pop the top item from the heap
        # The item is the second element of the tuple
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if not self.heap:
            raise IndexError("peek from an empty stack")
        
        # Return the item (second element of the tuple) without removing it
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

# Test the Stack implementation
stack = Stack()

# Push some items
stack.push(1)
stack.push(2)
stack.push(3)

# Pop items
print(stack.pop())  # Should print 3
print(stack.pop())  # Should print 2

# Push more items
stack.push(4)
stack.push(5)

# Peek
print(stack.peek())  # Should print 5

# Pop remaining items
print(stack.pop())  # Should print 5
print(stack.pop())  # Should print 4
print(stack.pop())  # Should print 1

# Try to pop from an empty stack
try:
    stack.pop()
except IndexError as e:
    print(f"Error: {e}")