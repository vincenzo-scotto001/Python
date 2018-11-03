# Chapter V problem VIII by Vincenzo Scotto Di Uccio

def main():
    print("Program starts here.")
    
    sq_ft =input("Enter the total amount of square feet please: ")

    paint_amount =input("Enter the paint price per gallon: ")

    sq_ft = input_valid(sq_ft)
    paint_amount = input_valid(paint_amount)
    
    calculate(sq_ft,paint_amount)

def calculate(sq_ft,paint_amount):
    
    gal = sq_ft / 112

    lab_hour = gal * 8

    paint_charge = gal * paint_amount

    lab_charge = lab_hour * 35

    total = paint_charge + lab_charge
    print(" The number of gallons of paint needed is: ", gal)
    print ("The hours of labor required is: ", lab_hour)
    print ("The cost of the paint is: ", paint_charge)
    print ("The labor charges are: ", lab_charge)
    print ("The total for all of this is: ", total)

def input_valid(a_str):

    value_s = 0
    error_s = 0
    make_f = 0

    while value_s == 0:
        error_s = 0
        for aChar in a_str:

            if (aChar >= '0' and aChar <= '9'):
                error_s = 0
            elif aChar == '.':
                make_f = 1
                
            else:
                error_s = 1
                break
        if error_s > 0:     
            a_str = input("Error, invalid data was entered, please the square feet and the paint amount: ")                 
            error_s = 0
        else:
            value_s = 1
    if make_f == 1:
        return float(a_str)
    else:
        return int(a_str)                      
main()
