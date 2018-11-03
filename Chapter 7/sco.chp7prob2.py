# Chapter VII problem II by Vincenzo Scotto Di Uccio

import random

lotterynumbers = []

x = 0

while x < 7:
    lotterynumbers.append(random.randint(0,9))
    x += 1

lotterynumbers.sort()

print ("The numbers are: ", lotterynumbers)



