"""
This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. 
They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer 
has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1]


"""

def calculate_bonuses(code_lines):
    n = len(code_lines)
    bonuses = [1] * n  # Initialize all bonuses to 1

    # Left to right pass
    for i in range(1, n):
        if code_lines[i] > code_lines[i-1]:
            bonuses[i] = bonuses[i-1] + 1

    # Right to left pass
    for i in range(n-2, -1, -1):
        if code_lines[i] > code_lines[i+1] and bonuses[i] <= bonuses[i+1]:
            bonuses[i] = bonuses[i+1] + 1

    return bonuses

# Test the function
code_lines = [10, 40, 200, 1000, 60, 30]
result = calculate_bonuses(code_lines)
print(result)  # Should output [1, 2, 3, 4, 2, 1]
