# Menu Driven Chapter VII problems III, IV and random by Vincenzo Scotto Di Uccio
import random
RAINFALL = "1"
NUMBER = "2"
QUIT = "3"

def main():
    x = 0

    while x != QUIT:
        valid = 0
        display_menu()

        x = input(" Enter your number(1-3): ")

        if x >= "1" and x <= "3":
            if x == RAINFALL:
                rainfall()
            elif x == NUMBER:
                number()
            elif x == QUIT:
                return
            else:
                print(" Please enter a valid input(1,2,3): ")
def rainfall():
    year = []
    months =["January","February","March","April","May", "June", "July", "August", "September","October", "November", "December"]
    for month in months:
        year.append(float(input(" Please enter rainfall for " + month  )))
    
    print(" Total rainfall is: " , sum(year))
    print(" Average rainfall is: " , sum(year)/2)
    print("Lowest rainfall is: ", min(year))
    print ("Highest rainfall is: ", max(year))
    
            
    
    



def number():
    list1= []
    total = 0
    for i in range(0,20):
        x = random.randint(0,100)
        list1.append(x)
        total += x
    print(list1)
    print("The least on the list: " ,min(list1))
    print("The max on the list: ", max(list1))
    print("The total of the list: " ,sum(list1))
    print("The average of the list: " ,sum(list1)/20)
    print("Another way of totaling: " , total)
    list1.sort()
    print(" The list from least to greatest: " ,list1)
    
    
    
    

    
def display_menu():
    print("1) Rainfall")
    print("2) Number")
    print("3) Quit")

main()
                
