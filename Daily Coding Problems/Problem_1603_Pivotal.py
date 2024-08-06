"""
This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.

"""

def count_set_bits(N):
    if N == 0:
        return 0
    
    # Find the largest power of 2 less than or equal to N
    power_of_2 = 1
    while power_of_2 * 2 <= N:
        power_of_2 *= 2
    
    # Calculate set bits
    return (
        # Count of set bits in numbers from 1 to largest power of 2
        (power_of_2 // 2) * (power_of_2 // 2) +
        # Most significant bit of all numbers from largest power of 2 to N
        (N - power_of_2 + 1) +
        # Recursively count set bits in the remaining range
        count_set_bits(N - power_of_2)
    )

# Test the function
for i in range(1, 17):
    print(f"Total set bits from 1 to {i}: {count_set_bits(i)}")
