# Chapter V problem X by Vincenzo Scotto Di Uccio


def main():
    feet =input("Please enter the amount of feet to be converted: ")
    feet = input_valid(feet)
    inches = feet * 12
    print( " Inches: ", inches)
    
    
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
            a_str = input("Error, please enter a valid input: ")                 
            error_s = 0
        else:
            value_s = 1
    if make_f == 1:
        return float(a_str)
    else:
        return int(a_str)                  

main()
    
































