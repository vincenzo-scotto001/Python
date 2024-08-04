"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""


import random
import math

def estimate_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(total_points):
        # Generate random x and y coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Calculate the distance from the origin (0, 0)
        distance = math.sqrt(x**2 + y**2)

        # Check if the point is inside the unit circle
        if distance <= 1:
            points_inside_circle += 1

    # Estimate pi
    pi_estimate = 4 * points_inside_circle / total_points

    return pi_estimate

# Run the estimation with a large number of points
num_points = 1000000
estimated_pi = estimate_pi(num_points)

print(f"Estimated π: {estimated_pi:.3f}")
print(f"Actual π: {math.pi:.3f}")