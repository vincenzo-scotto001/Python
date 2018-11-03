# Vincenzo Scotto Di Uccio Chapter II problem VI
# Problem VI is a Sales Tax problem

purchase = float(input( " Please enter the amount of the purchase: "))

state_tax = 0.05
county_tax = 0.025

total_state_tax = state_tax * purchase
total_county_tax = county_tax * purchase

total_sales_tax = total_state_tax + total_county_tax

total_amount = purchase + total_sales_tax

print(" The state tax is: ", total_state_tax)
print(" The county tax is: ", total_county_tax)
print(" The total sales tax is: ", total_sales_tax)
print (" The total amount of the purchase is: ", total_amount)
