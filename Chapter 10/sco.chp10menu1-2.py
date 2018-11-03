# Chapter X problems I,II in menu by Vincenzo Scotto Di Uccio

PET = '1'
CAR = '2'
STOP = '3'

import Pet
import Vehicle
def main():
    x = 0
    while x!= STOP:
        valid = 0
        display_menu()

        x = input('Enter your number(1-3): ')
        if x >= '1' and x <= '3':
            if x == '1':
                animal()
            elif x == '2':
                car()
            elif x == '3':
                return
            else:
                print('Please enter a valid input: ')
def animal():
    
    name = input('What is the name of the pet: ')
    animal_type = input('What type of pet is it: ')
    age = int(input('How old is your pet: '))
    pets = Pet.Pet(name, animal_type, age)
    print('This will be added to the records. ')
    print('Here is the data you entered:')
    print('Pet Name: ', pets.get_name())
    print('Animal Type: ', pets.get_animal_type())
    print('Age: ', pets.get_age())


    
def car():
    import random

    year = input('car year: ')
    make = input('car make: ')

    my_car = Vehicle.Vehicle(year,make)

    acc = random.randint(1,10)
    brk = random.randint(1,5)

    for b in range(0,acc):
        my_car.accel()
    for c in range(0,brk):
        my_car.brake()
    print('Final Velocity: ', my_car.get_speed())
    print('Accelerations: ', acc)
    print('Decelerations: ', brk)
        
        
        
    
    
    

def display_menu():
    print('1) Pet Class')
    print('2) Car Class')
    print('3) Quit')
    
main()
