"""
Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct, 
find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. 
It is guaranteed that the first and last elements are lower than all others.

"""


def find_peak_element(arr):
    # Helper function to perform the binary search
    def binary_search_peak(left, right):
        # Base case: if the search space is reduced to one element
        if left == right:
            return left
        
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the middle element is greater than the next element
        # then the peak must be in the left half (including mid)
        if arr[mid] > arr[mid + 1]:
            return binary_search_peak(left, mid)
        else:
            # Otherwise, the peak must be in the right half (excluding mid)
            return binary_search_peak(mid + 1, right)
    
    # Perform binary search to find the peak element
    return binary_search_peak(0, len(arr) - 1)

# Example usage
arr = [6, 7, 1, 2, 3, 4, 5]
peak_index = find_peak_element(arr)
print(f"Peak element is at index {peak_index}, value: {arr[peak_index]}")
