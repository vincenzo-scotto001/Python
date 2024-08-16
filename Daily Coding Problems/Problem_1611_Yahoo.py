"""
You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

"""


def smallest_string_after_moves(s, k):
    n = len(s)
    
    # Convert the string to a list for easier manipulation
    s = list(s)
    
    # Create the result string
    result = []
    
    for i in range(n):
        # Find the smallest character in the next k characters
        best = min(s[:min(k, len(s))])
        
        # Find the index of this smallest character
        idx = s.index(best)
        
        # Add this character to the result
        result.append(best)
        
        # Remove this character from the original string
        s.pop(idx)
        
        # If we've removed a character before the kth position,
        # we need to decrease k to maintain the window
        if idx < k:
            k -= 1
        
        # If k becomes 0, we can't make any more moves
        if k == 0:
            result.extend(s)
            break
    
    # Convert the result list back to a string
    return ''.join(result)

# Test the function
print(smallest_string_after_moves("daily", 1))  # Should print "ailyd"
print(smallest_string_after_moves("cba", 1))    # Should print "acb"
print(smallest_string_after_moves("dcba", 4))   # Should print "abcd"