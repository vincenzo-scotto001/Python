# Given an array of integers, 
# return a new array such that each element at index i of the 
# new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6]

def array(uber):
    product = 1
    for n in uber:
        product *= n
    for i in range(len(uber)):
        uber[i] = product / uber[i]





uber = [1, 2, 3, 4, 5]
array(uber)
print(uber)