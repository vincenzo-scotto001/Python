"""
This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, 
rotate the array to the right k elements in-place.

"""


def rotate_array(arr, k):
    """
    Rotate the array to the right by k elements in-place.
    
    Args:
    arr (list): The input array to be rotated
    k (int): The number of positions to rotate right
    
    Returns:
    None (the array is modified in-place)
    """
    n = len(arr)
    
    # Handle the case where k is larger than the array length
    k = k % n
    
    # If k is 0 or equal to the array length, no rotation is needed
    if k == 0:
        return
    
    # Reverse the entire array
    reverse(arr, 0, n - 1)
    
    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    
    # Reverse the remaining n-k elements
    reverse(arr, k, n - 1)

def reverse(arr, start, end):
    """
    Reverse the elements in the array between start and end indices (inclusive).
    
    Args:
    arr (list): The array to be partially reversed
    start (int): The starting index
    end (int): The ending index
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Test the function
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Original array: {arr}")
rotate_array(arr, k)
print(f"Array after rotating right by {k} elements: {arr}")