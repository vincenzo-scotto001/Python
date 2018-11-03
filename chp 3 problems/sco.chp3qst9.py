# Chapter III problem IX roulette wheel colors by Vincenzo Scotto Di Uccio

pocket_number = int(input(" Please put a number between 0-36: "))

 

while (pocket_number < 0 or pocket_number > 36):
    
    if pocket_number < 0 or pocket_number > 36:
        print("False, not a valid number.")

    pocket_number = int(input(" Please put a number between 0-36: "))

if pocket_number == 0:
    print ("green")

elif pocket_number > 0 or pocket_number < 11:
    if pocket_number % 2 != 0:
        print ("red")
    else:
        print ("black")
elif pocket_number > 11 or pocket_number < 18:
    if pocket_number % 2 != 0:
        print ("black")
    else:
        print ("red")
elif pocket_number > 19 or pocket_number < 28:
    if pocket_number % 2 != 0:
        print ("red")
    else:
        print ("black")
elif pocket_number > 29 or pocket_number < 36:
    if pocket_number % 2 != 0:
        print ("black")
    else:
        print ("red")



                



