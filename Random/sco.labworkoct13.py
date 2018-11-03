# October lab work 6-8 by Vincenzo Scotto Di Uccio


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

    


    
