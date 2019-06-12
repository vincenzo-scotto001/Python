# This problem was asked by Google.
# The area of a circle is defined as πr^2. 
# Estimate π to 3 decimal places using a Monte Carlo method.
# The basic equation of a circle is x2 + y2 = r2.
# pi/4 = N in / N total
# pi = 4 (N in / N total)



import math
import numpy as np
import random

dots = 100000
# dots = int(input('Give me a number of dots: '))
inside = 0

def pi_estimate(dots, inside):
    for i in range(0, dots):
        x,y = random.random()**2, random.random()**2

        if math.sqrt(x+y) < 1:
            inside += 1

    pi = float(inside)/dots * 4
    return (f"{pi:.3f}")
#print(pi)

pi_estimate(dots, inside)


