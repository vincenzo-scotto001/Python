"""
This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. 
Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

"""

def find_busiest_period(entries):
    # Sort the entries by timestamp
    sorted_entries = sorted(entries, key=lambda x: x['timestamp'])
    
    max_people = 0
    current_people = 0
    busiest_start = None
    busiest_end = None
    
    for i, entry in enumerate(sorted_entries):
        # Update the number of people based on the entry type
        if entry['type'] == 'enter':
            current_people += entry['count']
        else:  # 'exit'
            current_people -= entry['count']
        
        # Check if this is the new maximum
        if current_people > max_people:
            max_people = current_people
            busiest_start = entry['timestamp']
            # The end of the busiest period is the next timestamp or the last timestamp if there is no next
            busiest_end = sorted_entries[i+1]['timestamp'] if i+1 < len(sorted_entries) else entry['timestamp']
    
    return (busiest_start, busiest_end)

# Test the function
entries = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526580382, "count": 2, "type": "exit"},
    {"timestamp": 1526579938, "count": 6, "type": "enter"},
    {"timestamp": 1526579943, "count": 1, "type": "enter"},
    {"timestamp": 1526580345, "count": 5, "type": "exit"}
]

busiest_period = find_busiest_period(entries)
print(f"The busiest period is from {busiest_period[0]} to {busiest_period[1]}")