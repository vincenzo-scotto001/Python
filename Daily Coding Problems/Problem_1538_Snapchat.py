"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

def min_classrooms(intervals):
    # Separate start and end times
    start_times = sorted(interval[0] for interval in intervals)
    end_times = sorted(interval[1] for interval in intervals)

    rooms_needed = 0  # Current number of rooms needed
    max_rooms = 0     # Maximum number of rooms needed at any point
    start_ptr = 0     # Pointer for start times
    end_ptr = 0       # Pointer for end times

    # Sweep through all times
    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            # A new class is starting before the earliest ending class
            rooms_needed += 1
            start_ptr += 1
        else:
            # A class has ended
            rooms_needed -= 1
            end_ptr += 1

        # Update max_rooms if necessary
        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms

# Test the function
intervals = [(30, 75), (0, 50), (60, 150)]
print(f"Minimum number of rooms required: {min_classrooms(intervals)}")