"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

"""

def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Modify the array to ignore non-positive and out-of-range numbers
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark existing numbers
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first missing positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If all numbers from 1 to n are present, return n + 1
    return n + 1

# Test cases
print(first_missing_positive([3, 4, -1, 1]))  # Should print 2
print(first_missing_positive([1, 2, 0]))      # Should print 3
print(first_missing_positive([7, 8, 9, 11, 12]))  # Should print 1