# Lab for december 8th combination of program I and III by Vincenzo Scotto Di Uccio

import pickle
import Pet
import people
def main():
    PET = 1
    PEOPLE = 2
    QUIT = 3
    choice= 0
    while choice != QUIT:
        choice = display_menu()
        if choice == PET:
            pet_main()
        elif choice == PEOPLE:
            people_main()
    print('End')
def display_menu():
    PET = 1
    PEOPLE = 2
    QUIT = 3
    print()
    print('MENU')
    print('----------------------------')
    print('1) Pet')
    print('2) People')
    print('3) Quit ')
    c = int(input('Enter your choice: '))
    while c <PET  or c > QUIT:
        c = int(input('Enter a valid choice: '))

    return c
def pet_main():
    ADD = 1
    DEL = 2
    STOP = 3
    my_pet = load_pet()
    choice = 0
    while choice != STOP:
        choice = pet_dis()
        if choice == ADD:
            add(my_pet)
        elif choice == DEL:
            delete(my_pet)
    save_pet(my_pet)
    
    
def load_pet():
    file = 'pet.txt'
    try:
        infile = open('pet.txt', 'rb')
        pets_dic = pickle.load(infile)
        infile.close()
    except IOError:
        pets_dic = {}
    return pets_dic
def pet_dis():
    ADD = 1
    QUIT = 3
    print('1)Add pet')
    print('2)Delete pet')
    print('3)Quit')
    x = int(input('Enter your choice: '))

    while x < ADD or x > QUIT:
        x = int(input('Enter a valid choice: '))
    return x

def add(my_pet):
    name = input('Name: ')
    animal_type = input('breed: ')
    age = input('age: ')
    y = Pet.Pet(name, animal_type , age)
    if name not in my_pet:
        my_pet[name] = y
        print('The entry has been added')
    else:
        print('The entry already exists.')
def delete(my_pet):
    name = input('Name: ')
    if name in my_pet:
        del my_pet[name]
        print('%s has been deleted from the contract list.' %name)
    else:
        print("The name %S is not found in the contact list." %name)
def people_main():
    ADD = 1
    DEL = 2
    STOP = 3
    my_people = load_people()
    choice = 0
    while choice != STOP:
        choice = ppl_dis()
        if choice == ADD:
            add2(my_people)
        elif choice == DEL:
            delete2(my_people)
    save_pets(my_people)
def load_people():
    file = 'people.txt'
    try:
        infile = open('people.txt', 'rb')
        pets_dic = pickle.load(infile)
        infile.close()
    except IOError:
        pets_dic = {}
    return pets_dic
    
def ppl_dis():
    ADD = 1
    QUIT = 3
    print('1)Add person')
    print('2)Delete person')
    print('3)Quit')
    x = int(input('Enter your choice: '))

    while x < ADD or x > QUIT:
        x = int(input('Enter a valid choice: '))
    return x


def add2(my_people):
    name = input('Name: ')
    addr = input('Address: ')
    age = input('Age: ')
    phone = input('Phone: ')
    x = people.Personal(name, address , age, phone)
    if name not in my_pet:
        my_people[name] = x
        print('The entry has been added')
    else:
        print('The entry already exists.')
    
    
def delete2(my_people):
    name = input('Name: ')
    if name in my_people:
        del my_people[name]
        print('%s has been deleted from the contract list.' %name)
    else:
        print("The name %S is not found in the contact list." %name)
    
main()


    
        
    
