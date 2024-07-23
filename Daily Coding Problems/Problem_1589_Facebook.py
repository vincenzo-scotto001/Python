"""
This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:


"""


# function that uses a stacked based approach to solve this problem.
def min_quxes_remaining(quxes):

    # create empty stack and set up the color map.
    stack = []
    color_map = {'R': 'G', 'G': 'B', 'B': 'R'}
    

    # for loop that goes through the input of quxes, essentially we are checking every pairing
    # if the pairing are different, they are removed and become the other color. If not, we move on.
    for qux in quxes:
        if len(stack) >= 2:
            print(f'This is the current stack: {stack}')
            last = stack.pop()
            second_last = stack.pop()
            
            if qux != last and qux != second_last and last != second_last:
                # Transform the last two Quxes with the current one
                new_color = [c for c in color_map if c not in [qux, last]][0]
                stack.append(new_color)
                print(f'Transformation possible: {qux} from {last} and {second_last}')

            else:
                # No transformation possible, push back and add current
                stack.append(second_last)
                stack.append(last)
                stack.append(qux)
                print(f'Not transformation: {qux}')
        else:
            stack.append(qux)
    
    return len(stack)

# Test the function
input_quxes = ['R', 'G', 'B', 'G', 'B']
result = min_quxes_remaining(input_quxes)
print(f"Minimum number of Quxes remaining: {result}")