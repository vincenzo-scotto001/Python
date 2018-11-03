#Analysis worksheet problem V by vincenzo scotto di uccio

total = int(input(" Please enter the total: "))

pennies = total %50 %25 %10 %5 // 1

nickles = total %50 %25 %10 // 5

dimes = total %50 %25 // 10

quarters = total % 50 // 25

halves = total // 50

print (" Number of pennies: ", pennies)
print (" Number of nickles: ", nickles)
print (" Number of dimes: ", dimes)
print (" Number of quarters: ", quarters)
print (" Number of halves: ", halves)

