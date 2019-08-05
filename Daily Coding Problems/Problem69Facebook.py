# Given a list of integers, return the largest product that can be made by 
# multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], 
# we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.

fb = [-10,-10,5,2]

grand_total= 0

for i in range(len(fb)):
    for x in range(len(fb)):
        for y in range(len(fb)):
            total = fb[i]*fb[x]*fb[y]
            if total > grand_total:
                grand_total = total
print(grand_total)