"""

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""


def is_one_to_one_mapping(s1: str, s2: str) -> bool:
    """
    Determine whether there exists a one-to-one character mapping from s1 to s2.

    Args:
    s1 (str): The first string
    s2 (str): The second string

    Returns:
    bool: True if a one-to-one mapping exists, False otherwise
    """
    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False

    # Dictionary to store the mapping from s1 to s2
    char_map = {}
    # Set to keep track of used characters in s2
    used_chars = set()

    # Iterate through both strings simultaneously
    for c1, c2 in zip(s1, s2):
        # If c1 is already mapped
        if c1 in char_map:
            # Check if it's mapped to the same character in s2
            if char_map[c1] != c2:
                return False
        else:
            # If c2 is already used for another character in s1
            if c2 in used_chars:
                return False
            # Create a new mapping
            char_map[c1] = c2
            used_chars.add(c2)

    # If we've made it through the entire strings, a valid mapping exists
    return True


# Test cases
print(is_one_to_one_mapping("abc", "bcd"))  # Should return True
print(is_one_to_one_mapping("foo", "bar"))  # Should return False
print(is_one_to_one_mapping("bar", "foo"))  # Should return True
print(is_one_to_one_mapping("hello", "world"))  # Should return False
print(is_one_to_one_mapping("abba", "dccd"))  # Should return True
print(is_one_to_one_mapping("abba", "dcce"))  # Should return False