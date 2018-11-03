# Chapter V problem 7 by Vincenzo Scotto Di Uccio


def main():
   print("Program starts here.")
   
   a_sold = input("How many class A were sold: ")

   b_sold = input("How many class B were sold: ")

   c_sold = input("How many class C were sold: ")

   a_sold = input_valid(a_sold)
   b_sold = input_valid(b_sold)
   c_sold = input_valid(c_sold)

   calculate(a_sold,b_sold,c_sold)


def calculate(class_a, class_b, class_c):
    total = class_a *20 +class_b *15 + class_c * 10
    print("Your total income from the ticket sales are: ", total)

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
