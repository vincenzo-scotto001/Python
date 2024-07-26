"""
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.

"""


def intersection_area(rect1, rect2):
    # Unpack the rectangle data
    x1, y1 = rect1["top_left"]
    w1, h1 = rect1["dimensions"]
    x2, y2 = rect2["top_left"]
    w2, h2 = rect2["dimensions"]

    # Calculate the coordinates of the bottom right corners
    # Remember: y decreases as we go down in 2D graph coordinates
    bottom_right1 = (x1 + w1, y1 - h1)
    bottom_right2 = (x2 + w2, y2 - h2)

    # Find the coordinates of the intersection rectangle
    # The left edge is the rightmost of the two left edges
    left = max(x1, x2)
    # The right edge is the leftmost of the two right edges
    right = min(bottom_right1[0], bottom_right2[0])
    # The top edge is the lower of the two top edges
    top = min(y1, y2)
    # The bottom edge is the higher of the two bottom edges
    bottom = max(bottom_right1[1], bottom_right2[1])

    # If the rectangles don't intersect, return 0
    if left >= right or top <= bottom:
        return 0

    # Calculate and return the area of intersection
    width = right - left
    height = top - bottom
    return width * height

# Example usage
rect1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3)  # width, height
}

rect2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3)  # width, height
}

result = intersection_area(rect1, rect2)
print(f"The area of intersection is: {result}")