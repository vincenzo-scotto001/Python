# Chapter III problem XIII shipping charges by Vincenzo Scotto Di Uccio


weight = float(input( "Please enter the weight of your package: "))

if weight <= 2 and weight > 0:
    weight = weight * 1.50
    print (" Your rate per pound is: $1.50", " Your total is: " , weight)
if weight > 2 and weight <=6:
    weight = weight * 3.00
    print (" Your rate per pound is: $3.00" , "Your total is: " , weight)
if weight > 6 and weight <=10:
    weight = weight * 4.00
    print (" Your rate per pound is: 4.00" , "Your total is: ", weight)
if weight > 10:
    weight = weight *4.75
    print (" Your rate per pound is: 4.75" , "Your total is: ", weight)
else:
    print ("Error, invalid number of punds.")
    
    
