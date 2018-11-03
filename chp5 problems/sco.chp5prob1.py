# Chapter V problem I by Vincenzo Scotto Di Uccio

def main():
    print("My program starts here")
    
    kilometers =input("Enter the kilometer: ")
    
    kilometers = input_valid(kilometers)

    print("The kilometers you entered ", kilometers)

    a_str = kilometers * 0.6214

    print("You have miles: ",a_str)
def input_valid(a_str):
    value_s = 0
    error_s = 0
    make_f = 0

    while value_s ==0:
        error_s = 0
        for aChar in a_str:

            if (aChar >= "0" and aChar <= "10"):
                error_s = 0
            elif aChar == ".":
                make_f = 1
            else:
                error_s = 1
                break
        if error_s > 0:
            a_str =input("Error, input value not valid. Try again: ")
            error_s = 0
        else:
            value_s =1
        if make_f == 1:
            return float(a_str)
        else:
            return int(a_str)
            
main()
