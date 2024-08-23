"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

def num_decodings(message):
    """
    Count the number of ways a message can be decoded.
    
    Args:
    message (str): The encoded message
    
    Returns:
    int: The number of ways the message can be decoded
    """
    # Check if the message is empty or starts with '0'
    if not message or message[0] == '0':
        return 0
    
    n = len(message)
    
    # Initialize dp array
    # dp[i] represents the number of ways to decode the message up to index i
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # Empty string
    dp[1] = 1  # First character
    
    for i in range(2, n + 1):
        # Check if the current digit is valid (not '0')
        if message[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Check if the last two digits form a valid number (10-26)
        two_digit = int(message[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

# Test cases
test_cases = ['111', '12', '226', '06', '10', '27']
for case in test_cases:
    print(f"Message: {case}, Number of decodings: {num_decodings(case)}")