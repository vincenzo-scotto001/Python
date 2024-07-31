"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

"""

def power_set(s):
    # Convert the input to a list if it's not already
    s = list(s)
    
    def generate_subsets(index, current_subset):
        # Base case: if we've processed all elements, add the current subset to our result
        if index == len(s):
            return [current_subset]
        
        # Recursive cases:
        # 1. Don't include the current element
        subsets = generate_subsets(index + 1, current_subset.copy())
        
        # 2. Include the current element
        current_subset.append(s[index])
        subsets += generate_subsets(index + 1, current_subset.copy())
        
        return subsets

    # Start the recursion with an empty subset and index 0
    return generate_subsets(0, [])

# Test the function
set_input = {1, 2, 3}
result = power_set(set_input)

# Print the result
print("Power set of", set_input, "is:")
for subset in result:
    print(subset)

# Print the total number of subsets
print("Total number of subsets:", len(result))