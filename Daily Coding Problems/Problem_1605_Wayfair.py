"""

This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.
"""



def count_tilings(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Initialize dp array to store solutions for subproblems
    # dp[i] represents the number of ways to tile a 2 x i board
    dp = [0] * (n + 1)
    
    # Set base cases
    dp[0] = 1  # Empty board
    dp[1] = 1  # Only one way to tile a 2 x 1 board (vertical domino)
    
    # Fill dp array using the recurrence relation
    for i in range(2, n + 1):
        # Recurrence relation:
        # 1. Place a vertical domino: dp[i-1] ways
        # 2. Place two horizontal dominoes: dp[i-2] ways
        # 3. Place a tromino: dp[i-2] ways
        # Total: dp[i-1] + 2 * dp[i-2]
        dp[i] = dp[i-1] + 2 * dp[i-2]
    
    # Return the total number of ways to tile a 2 x n board
    return dp[n]

# Test the function for n from 0 to 9
for i in range(10):
    print(f"f({i}) = {count_tilings(i)}")