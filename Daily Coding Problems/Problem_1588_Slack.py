"""
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.


"""


def num_ways(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    len_of_matrix = len(matrix)
    len_of_row = len(matrix[0])
    print(len_of_matrix, len_of_row)
    
    # Initialize the dp matrix
    matrix_space = [[0] * len_of_row for _ in range(len_of_matrix)]
    
    # Start point
    matrix_space[0][0] = 1
    
    # Fill the dp matrix
    for i in range(len_of_matrix):
        for j in range(len_of_row):
            if matrix[i][j] == 1:
                matrix_space[i][j] = 0  # No way to go through walls
            else:
                if i > 0:
                    matrix_space[i][j] += matrix_space[i-1][j]
                if j > 0:
                    matrix_space[i][j] += matrix_space[i][j-1]
    
    return matrix_space[len_of_matrix-1][len_of_row-1]

# Test the function with the given example
matrix = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0]
]

print(num_ways(matrix))
