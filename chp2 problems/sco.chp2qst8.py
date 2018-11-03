# Vincenzo Scotto Di Uccio chapter II problem VIII
# This problem is about tip, tax and total

amount = float(input( " Please enter the amount: "))

tip = amount * 0.18

sales_tax = amount * 0.07

total = amount + tip + sales_tax

print (" The tip amount is: ", tip)
print (" The sales tax amount is: ", sales_tax)
print (" The total amount is: ", total)
