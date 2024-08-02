"""
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

"""


def count_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    islands = 0

    def dfs(i, j):
        # depth first search
        # Check if we're out of bounds or if this cell is water
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0:
            return

        # Mark this cell as visited by setting it to 0
        matrix[i][j] = 0

        # Recursively visit all adjacent cells
        dfs(i-1, j)  # Up
        dfs(i+1, j)  # Down
        dfs(i, j-1)  # Left
        dfs(i, j+1)  # Right

    # Iterate through each cell in the matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands

# Test the function
matrix = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

print(f"Number of islands: {count_islands(matrix)}")