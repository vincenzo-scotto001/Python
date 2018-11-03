# Chapter V problem VI by Vincenzo Scotto Di Uccio

def main():

    f_g = input("Enter the total amount of fat grams: ")

    c_g = input("Enter the total amount of carbohydrate grams: ")


    f_g = input_valid(f_g)
    c_g =input_valid(c_g)
    
    calculate(f_g,c_g)

def calculate(fat,carb):

    cal_fat = fat * 9

    cal_carb = carb *4

    print("Calories from fat is: ", cal_fat)
    print ("Calories from carbohydrates: ", cal_carb)

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
            a_str = input("Error, invalid data entered, please try again. Enter the fats than the carbohydrates :")

            error_s = 0
        else:
            value_s = 1
    if make_f == 1:
        return float(a_str)
    else:
        return int(a_str)                                     

main()
