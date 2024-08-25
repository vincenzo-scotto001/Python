"""
This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. 
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, 
from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

from heapq import heappush, heappop

def first_n_regular_numbers(N):
    """
    Generate the first N regular numbers.
    
    A regular number is one whose only prime divisors are 2, 3, and 5.
    
    Args:
    N (int): The number of regular numbers to generate
    
    Returns:
    list: The first N regular numbers in ascending order
    """
    if N <= 0:
        return []
    
    # Initialize the result list with the first regular number
    regular_numbers = [1]
    
    # Use a min-heap to keep track of the next potential regular numbers
    heap = []
    
    # Initialize indices for 2, 3, and 5 multiples
    i2, i3, i5 = 0, 0, 0
    
    # Generate the next N-1 regular numbers
    for _ in range(1, N):
        # Calculate the next potential regular numbers
        next_2 = regular_numbers[i2] * 2
        next_3 = regular_numbers[i3] * 3
        next_5 = regular_numbers[i5] * 5
        
        # Push these potential numbers onto the heap
        heappush(heap, next_2)
        heappush(heap, next_3)
        heappush(heap, next_5)
        
        # Get the smallest number from the heap
        next_regular = heappop(heap)
        
        # Add it to our result list if it's not a duplicate
        if next_regular > regular_numbers[-1]:
            regular_numbers.append(next_regular)
        
        # Update the indices
        if next_regular == next_2:
            i2 += 1
        if next_regular == next_3:
            i3 += 1
        if next_regular == next_5:
            i5 += 1
    
    return regular_numbers

# Test the function
N = 20
result = first_n_regular_numbers(N)
print(f"The first {N} regular numbers are:")
print(result)