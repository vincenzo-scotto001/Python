"""

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

"""




class Iterator2D:
    def __init__(self, array_2d):
        self.array_2d = array_2d  # Store the 2D array
        self.row = 0  # Current row index
        self.col = 0  # Current column index

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements")

        # Skip any empty arrays
        while self.row < len(self.array_2d) and not self.array_2d[self.row]:
            self.row += 1
            self.col = 0

        # Get the current element
        result = self.array_2d[self.row][self.col]
        
        # Move to the next position
        self.col += 1

        # If we've reached the end of the current row, move to the next row and reset column
        if self.col >= len(self.array_2d[self.row]):
            self.row += 1
            self.col = 0

        return result

    def has_next(self):
        # Check if there are more elements
        while self.row < len(self.array_2d):
            if self.col < len(self.array_2d[self.row]):
                return True
            # If we've reached the end of a row, move to the next row
            self.row += 1
            self.col = 0
        return False

# Example usage
array_2d = [[1, 2], [3], [], [4, 5, 6]]
iterator = Iterator2D(array_2d)

# Iterate through all elements
while iterator.has_next():
    print(iterator.next(), end=' ')