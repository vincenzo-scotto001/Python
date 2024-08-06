"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

"""


def find_contiguous_sum(nums, K):
    # Initialize two pointers and the current sum
    left = 0
    current_sum = 0

    # Iterate through the list with the right pointer
    for right in range(len(nums)):
        # Add the current number to the sum
        current_sum += nums[right]

        # While the sum is greater than K, shrink the window from the left
        while current_sum > K and left < right:
            current_sum -= nums[left]
            left += 1

        # If we've found a sum equal to K, return the sublist
        if current_sum == K:
            return nums[left:right+1]

    # If no solution is found, return None or an empty list
    return None

# Test the function
nums = [1, 2, 3, 4, 5]
K = 9
result = find_contiguous_sum(nums, K)
print(f"Input: {nums}, K = {K}")
print(f"Output: {result}")

# Additional test cases
print(find_contiguous_sum([1, 2, 3, 4, 5], 15))  # Should return [1, 2, 3, 4, 5]
print(find_contiguous_sum([1, 2, 3, 4, 5], 7))   # Should return [3, 4]
print(find_contiguous_sum([1, 2, 3, 4, 5], 20))  # Should return None