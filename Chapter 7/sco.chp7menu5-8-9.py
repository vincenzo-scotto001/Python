# Chapter VII problems V, VIII, IX in menu by Vincenzo Scotto Di Uccio


CHARGE = "1"
NAME = "2"
POPULATION = "3"
QUIT = "4"

def main():
    x = 0

    while x != QUIT:
        valid = 0
        display_menu()

        x = input(" Enter your number(1-4): ")

        if x >= "1" and x <= "4":
            if x == CHARGE:
                charge()
            elif x == NAME:
                name()
            elif x == POPULATION:
                population()
            elif x == QUIT:
                return
            else:
                print(" Please enter a valid input(1,2,3,4): ")

def charge():
    file = open('charge_accounts.txt', 'r')
    list1 =[]
    for line in file:
        list1.append(line.rstrip('\n'))
    x =(input("Please enter a number: "))
    if x in list1:
        print("Valid")
    else:
        print("Invalid")

def name():
    
    boy_file = open('BoyNames.txt', 'r')
    boy_names = boy_file.readlines()
    
    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index = index + 1
    
    girl_file = open('GirlNames.txt', 'r')
    girl_names = girl_file.readlines()
    
    index = 0
    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n')
        index = index + 1

    
    user_name = input('What is your name? ')  
    if user_name in boy_names or user_name in girl_names:
        print('Your name is among the popular.')
    else:
        print('Your name is not among the popular.')


def population():
    list1=[]
    total = 0
    file = open('USPopulation.txt', 'r')
    for line in file:
        list1.append(int(line.rstrip('\n')))
       
    print('The average is: ' ,sum(list1)/40)
    print(' The highest population amount: ',max(list1))
    print(' The lost population amount: ' , min(list1))
    
    
     
    
    
    
        

def display_menu():
    print("1) Charge ")
    print("2) Name ")
    print("3) Population")
    print("4) Quit")
main()
    
