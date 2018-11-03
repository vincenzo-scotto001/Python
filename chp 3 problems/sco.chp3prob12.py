# Chapter III problem XII software sales by Vincenzo Scotto Di Uccio

total = float(input(" Please enter the amount of software that was purchased: "))
discount = 0
if total <= 10 and total >= 0:
    print (" Your total is: ", 99 * total, "You get no discount, sorry.")
elif total > 10 and total < 19:
    total = 99* total *.90
    discount = 99 * total *.10
    print (" Your total is: ", total ," Your discount is: ", discount)
elif total > 20 and total < 49:
    total = 99* total *.80
    discount = 99* total *.20
    print (" Your total is: ", total,
           "Your discount is: " , discount)
elif total > 50 and total < 99:
    total = 99* total *.70
    discount = 99* total * .30
    print (" Your total is: ", 99*total*.70,
           "Your discount is: ", discount)
elif total >= 100:
    total = 99* total *.60
    discount = 99 *total * .40
    print (" Your total is: ", total, 
           "Your discoutn is: " , discount)
else:
    print ("Error, invalid number.")
    
    
