"""
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

"""

class Solution:
    def __init__(self):
        self.buffer = []
        self.buffer_ptr = 0

    def readN(self, n):
        result = []
        
        # Keep reading until we have n characters or reach EOF
        while len(result) < n:
            # If buffer is empty, call read7() to fill it
            if self.buffer_ptr == 0:
                self.buffer = self.read7()
            
            # If read7() returns empty, we've reached EOF
            if not self.buffer:
                break
            
            # Calculate how many characters we can take from buffer
            chars_to_take = min(len(self.buffer) - self.buffer_ptr, n - len(result))
            
            # Add characters from buffer to result
            result.extend(self.buffer[self.buffer_ptr:self.buffer_ptr + chars_to_take])
            
            # Update buffer pointer
            self.buffer_ptr += chars_to_take
            
            # If we've used all characters in buffer, reset pointer
            if self.buffer_ptr == len(self.buffer):
                self.buffer_ptr = 0

        return ''.join(result)

    def read7(self):
        # This is a mock implementation of read7()
        # In a real scenario, this would be provided or would actually read from a file
        pass

# Example usage
solution = Solution()

# Mock the read7() method for testing
solution.read7 = lambda: "Hello w"
print(solution.readN(7))  # Output: "Hello w"

solution.read7 = lambda: "orld"
print(solution.readN(7))  # Output: "orld"

solution.read7 = lambda: ""
print(solution.readN(7))  # Output: ""

# Reset for a new test
solution = Solution()
solution.read7 = lambda: "Hello w"
print(solution.readN(5))  # Output: "Hello"

solution.read7 = lambda: "orld"
print(solution.readN(5))  # Output: " worl"

solution.read7 = lambda: ""
print(solution.readN(5))  # Output: "d"