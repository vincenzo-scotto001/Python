"""

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

"""

def longest_consecutive_ones(n):
    # Convert the integer to its binary representation
    binary = bin(n)[2:]  # [2:] to remove the '0b' prefix
    
    max_run = 0
    current_run = 0
    
    # Iterate through each digit in the binary representation
    for digit in binary:
        if digit == '1':
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    
    return max_run

# Test the function
print(longest_consecutive_ones(156))  # Should return 3
print(longest_consecutive_ones(7))    # Should return 3 (binary: 111)
print(longest_consecutive_ones(242))  # Should return 4 (binary: 11110010)
print(longest_consecutive_ones(15))   # Should return 4 (binary: 1111)
print(longest_consecutive_ones(0))    # Should return 0 (binary: 0)