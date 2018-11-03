#Chapter V problem IX by Vincenzo Scotto Di Uccio

def main():
    print("Program starts here.")
    
    sub_total=(input("Enter the total sales amount: "))

    print("Total sales tax is: ",sub_total)
    sub_total = input_valid(sub_total)
    state_sales_tax = input_valid(state_sales_tax)
    county_tax = input_valid(county_tax)
    state_sales_tax(sub_total)
    county_tax(sub_total)
    print ("State sales tax is: ", state_sales_tax(sub_total))

    print("County tax: ",county_tax(sub_total))

    print( "Your total sales tax is: ", state_sales_tax(sub_total) + county_tax(sub_total))

    
def state_sales_tax(sub_total):
    
    total = sub_total *0.05
    return total
    

def county_tax(sub_total):

    total = sub_total * 0.025
    return total
    
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
            a_str = input("Error, please enter valid data for the sales made: ")                 
            error_s = 0
        else:
            value_s = 1
    if make_f == 1:
        return float(a_str)
    else:
        return int(a_str)            


main()
