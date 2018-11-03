#Chapter III problem X money counting game by Vincenzo Scotto Di Uccio

print ("Please enter the amount of pennies, nickels, dimes and quarters:")

pennies = int(input("Enter pennies: "))

nickles = int(input("Enter nickles: "))

dimes = int(input("Enter dimes: "))

quarters = int(input("Enter quarters: "))

pennies = 0.01 * pennies

nickles = 0.05 * nickles

dimes = 0.10 * dimes

quarters = 0.25 * quarters 

total = pennies + nickles + dimes + quarters

if total == 1:
    print ("Good job you got a dollar.")
elif total < 1:
    print (" Sorry your total is less than one dollar.")
else:
    print ("Sorry your total is more than one dollar.")
    
