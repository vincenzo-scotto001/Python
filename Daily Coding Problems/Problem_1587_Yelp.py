"""

You are given an array of integers, where each element represents the maximum number of steps 
that can be jumped going forward from that element. 
Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], 
you should return 2, 
as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
"""

def min_jumps(arr):
    n = len(arr)
    
    # Edge case: If the array has only one element, no jumps are needed
    if n == 1:
        return 0

    # Initialize variables
    jumps = 1  # Start with the first jump
    max_reach = arr[0]  # The farthest point that can be reached with the current jump
    steps = arr[0]  # Steps remaining to reach the next jump

    # Traverse the array from the second element
    for i in range(1, n):
        # If we reach the end of the array
        if i == n - 1:
            return jumps

        # Update the farthest point that can be reached
        max_reach = max(max_reach, i + arr[i])
        
        # Decrement the steps as we move to the next element
        steps -= 1

        # If no steps remaining, we need to make a jump
        if steps == 0:
            jumps += 1
            steps = max_reach - i  # Update steps to the new farthest point

    return jumps

# Example usage
arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(min_jumps(arr))