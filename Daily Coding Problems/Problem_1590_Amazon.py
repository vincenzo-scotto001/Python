"""
Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.

"""

# the string
my_string = 'jiujitsu'

#empty list that will hold our letters
holder = []

# for loop to go through the string
for i in my_string:
    #if statement that says if the letter is already in the string, to start over, if it is not in the list, add it.
    if i in holder:

        'letter already in the word. starting over'
        holder = []
        holder.append(i)
        continue
    else:
        holder.append(i)

# print the outcome
print(f'holder should be filled with unique letters, with length: {len(holder)}')
print(holder)


"""
version 1 up above, quick to implement, easy to understand. Not the best for optimization. Doesnt solve every possible outcome, 
like for example, if we just removed the first j instead of deleting the whole 3 chars.
"""



def smallest_window_with_distinct_chars(s):

    # lets first get all the distinct chars
    distinct_chars = set(s)
    num_of_distinct = len(distinct_chars)

    # setting the initialized variables
    char_count = {}
    window_start = 0
    min_window_length = float('inf')
    unique_char_window = 0

    # for loop to go through the string
    for window_end in range(len(s)):
        if s[window_end] not in char_count:
            char_count[s[window_end]] = 1
            unique_char_window += 1
        else:
            char_count[s[window_end]] += 1

    
    # while loop to see if we have unique chars in our window
    while unique_char_window == num_of_distinct:
        # update the minimum length
        min_window_length = min(min_window_length , window_end - window_start + 1)

        # removing the leftmost char from the string in the window
        char_count[s[window_start]] -= 1
        if char_count[s[window_start]] == 0:
            del char_count[s[window_start]]
            unique_char_window -= 1
        window_start += 1

    return min_window_length if min_window_length != float('inf') else 0

print(smallest_window_with_distinct_chars("jiujitsu"))


"""
version two is more advance, takes care of a rolling window of unique chars. However we lose readability and simplicity. 
"""








