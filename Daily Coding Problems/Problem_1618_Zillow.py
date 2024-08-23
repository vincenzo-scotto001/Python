"""
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 
Create an algorithm to find the nth sevenish number.

"""

def nth_sevenish_number(n):
    """
    Find the nth sevenish number.
    
    A sevenish number is either a power of 7, or the sum of unique powers of 7.
    
    Args:
    n (int): The position of the sevenish number to find (1-indexed)
    
    Returns:
    int: The nth sevenish number
    """
    # List to store powers of 7
    powers_of_seven = []
    
    # Generate powers of 7 until we have enough to cover the nth sevenish number
    power = 0
    while len(powers_of_seven) < n.bit_length():
        powers_of_seven.append(7 ** power)
        power += 1
    
    # Initialize the result
    result = 0
    
    # Iterate through the binary representation of n
    for i in range(n.bit_length()):
        # If the i-th bit is set (1), add the corresponding power of 7 to the result
        if n & (1 << i):
            result += powers_of_seven[i]
    
    return result

# Test the function
for i in range(1, 11):
    print(f"The {i}th sevenish number is: {nth_sevenish_number(i)}")
