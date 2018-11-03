# Vincenzo Scotto Di Uccio chapter II problem IV
def main():
    

    item1 = input(" Enter total for item one: ")

    item2 = input(" Enter total for item two: ")

    item3 = input(" Enter total for item three: ")

    item4 = input(" Enter total for item four: ")

    item5 = input(" Enter total for item five: ")

    item1=input_valid(item1)
    item2=input_valid(item2)
    item3=input_valid(item3)
    item4=input_valid(item4)
    item5=input_valid(item5)

    sub_total = item1 + item2 + item3 + item4 + item5

    sale_tax = sub_total * 0.07

    total = sale_tax + sub_total

    print (" The subtotal is: ", sub_total)
    
    print (" The sales tax is: ", sale_tax)

    print (" The total is: ", total)

    
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
            a_str = input("Error, invalid input data, please put in the data again(class A, Class B, and Class C: ")                 
            error_s = 0
        else:
            value_s = 1
    if make_f == 1:
        return float(a_str)
    else:
        return int(a_str)
main()
