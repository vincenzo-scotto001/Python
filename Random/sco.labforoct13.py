# October 13th lab work 6-7 and 6-8 program by Vincenzo Scotto Di Uccio

import random

x = int(input(" How many random numbers will the file hold: "))

file = open("numbers.txt", "w")
tea = 0
while tea < x:
    rand_num = random.randint(1,500)
    file.write(str(rand_num)+ "\n")
    tea += 1
file.close()

file = open("numbers.txt", "r")

line = file.readline()

total = 0

travis = 0

while line != '':
    x = int(line)
    print (x)
    total += x
    travis += 1
    line = file.readline()



print (" Total of the numbers: ", total)
print (" Total numbers: " , travis)

