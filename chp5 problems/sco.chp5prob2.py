# Chapter V problem II by Vincenzo Scotto Di Uccio

def main():
    print("Program starts here.")
    
    sub_total=(input("Purchase amount: "))

    
    sub_total = input_valid(sub_total)
    state_sales_tax(sub_total)

    county_tax(sub_total)
    
    total = 0
def state_sales_tax(sub_total):
    print("In state sales tax" )
    total = sub_total *0.07
    

    print ("State sales tax is: ",total)

def county_tax(sub_total):
    print("In county tax")
    total = sub_total * 0.02

    print("County tax: ",total)


def input_valid(a_str):
    value_s = 0
    error_s = 0
    make_f = 0

    while value_s ==0:
        error_s = 0
        for aChar in a_str:
            if aChar >= "0" and aChar <= "9":
                error_s = 0
            elif aChar == ".":
                make_f = 1
            else:
                error_s = 1
                break

        if error_s > 0:
            a_str = input("Error, invalid data entered, please try again: ")
            error_s = 0
        else:
            value_s = 1
    if make_f ==1:
        return float(a_str)
    else:
        return int(a_str)
main()
