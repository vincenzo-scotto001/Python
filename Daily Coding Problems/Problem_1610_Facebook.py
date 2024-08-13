"""

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""


import random

def pick_random_element(stream):
    selected = None
    for i, element in enumerate(stream, start=1):
        if random.randint(1, i) == 1:
            selected = element
    return selected

# Example usage:
def stream_generator():
    # This is just a simulation of a data stream
    for i in range(1, 1000001):  # Simulating a million elements
        yield f"Element {i}"

# Pick a random element
result = pick_random_element(stream_generator())
print(f"Randomly selected: {result}")