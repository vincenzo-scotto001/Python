"""
Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” 
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

"""

def letter_combinations(digits, mapping):
    if not digits:
        return []

    # Helper function to perform backtracking
    def backtrack(index, path):
        # If the current path length is equal to the digits length, we have a complete combination
        if index == len(digits):
            combinations.append(''.join(path))
            return

        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        possible_letters = mapping[current_digit]

        # Iterate through each letter and proceed with the next digit
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # backtrack

    combinations = []
    backtrack(0, [])
    return combinations

# Example usage
mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
digits = "23"
result = letter_combinations(digits, mapping)
print(result)  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
