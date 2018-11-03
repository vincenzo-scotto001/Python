# Menu driven problem with two programs by Vincenzo Scotto Di Uccio
import math
import random
INTEGER = "1"
FALLING_DISTANCE = "2"
FALLING_DISTANCE_2 ="3" 
STOP = "4"


def main():
    x = 0
    while x != STOP:
        valid = 0
        display_menu()

        x = input("Enter your number(1-4): ")
        if x >= "1" and x <= "4":
            if x == INTEGER:
                int_calc()
            elif x == FALLING_DISTANCE:
                fall_dist()
            elif x == FALLING_DISTANCE_2:
                fall_dist2()
            else:
                print ("Please enter a valid number(1,2,3,4): ")

def int_calc():
    num1 = random.randint(1,100)
    
    num2 = random.randint(1,100)
    print(" The first number is: ", num1)
    print (" The second numebr is: ",num2)

    if num1 > num2:
        print(num1, "is bigger than", num2)
    else:
        print(num2, "is bigger than",num1)
    
    

def fall_dist():
    time = int(input(" How long has your object been falling for in seconds: "))

    d = 0.5 * 9.8 * (time**2)
    print(" Your object fell,",d,"m in",time,"s")
def fall_dist2():

    for c in range(1,11):
        d = 0.5 * 9.8 *(c**2)
        print ("The falling distance is" , format(d,",.2f"),"m",sep=" ")
    

def display_menu():
    print (" MENU ")
    print (" 1) Random integer program")
    print (" 2) falling distance program")
    print (" 3) falling distance 1-10 program")
    print (" 4) STOP")
main()
