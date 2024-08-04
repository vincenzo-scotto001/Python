"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

"""

def count_paths(N, M):
    # Create a matrix to store the number of ways to reach each cell
    # Initialize with 1 for the first row and first column
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(M)] for i in range(N)]

    # Fill the dp matrix
    for i in range(1, N):
        for j in range(1, M):
            # Number of ways to reach current cell is sum of ways to reach
            # the cell above and the cell to the left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # Return the bottom-right cell which contains the total number of ways
    return dp[N-1][M-1]

# Test cases
print(f"2x2 matrix: {count_paths(2, 2)} ways")  # Should print 2
print(f"5x5 matrix: {count_paths(5, 5)} ways")  # Should print 70



def count_paths_optimized(N, M):
    # Create a 1D array to store the number of ways for the current row
    dp = [1] * M

    for i in range(1, N):
        for j in range(1, M):
            # Update dp[j] to be the sum of the current dp[j] (which is the value from the cell above)
            # and dp[j-1] (which is the value from the cell to the left)
            dp[j] += dp[j-1]

    return dp[M-1]