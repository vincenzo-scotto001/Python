# Chapter X problem VI by Vincenzo Scotto Di Uccio
import pickle
import os.path
import Employee
LOOK = 1
ADD = 2
CHAN = 3
DEL = 4
QUIT = 5

def main():
    
    my_emp = load_emp()
    x = 0
    
    while x != QUIT:
        valid = 0
        display_menu()

        x = int(input('Enter your number(1-5): '))

        if x >=1 and x <= 5:
            if x == LOOK:
                look()
            elif x == ADD:
                add()
            elif x == CHAN:
                chan()
            elif x == DEL:
                dele()
            elif x == QUIT:
                return
            else:
                print('Please enter a valid number: ')
    save_emp(my_emp)
def load_emp():
    try:
        file = open('employee.txt','rb')
        emp_dict = pickle.load(file)
        file.close()
    except IOError:
        emp_dict = {}
    return emp_dict
def look():
    ID = int(input(' Please enter ID number: '))
    print(my_emp.get(name, 'Not found'))
          
    
def add():
    name = input('Name : ')
    IDnum =int(input('ID number: '))
    Dep = input('Department: ')
    JobTi =input('Job Title: ')
    data = Employee.employee(name,IDnum,Dep,JobTi)
    if IDnum not in my_emp:
        my_emp[IDnum] = data
        print('Data has been entered.')
    else:
        print(' Data is already exists. ')

def chan():
    IDnum = int(input('Please enter ID number: ' ))
    if IDnum in my_emp:
        name = input('Enter new name: ')
        Dep = input(' Enter new department: ')
        JobTi = input('Enter new job title: ')
        my_emp[IDnum] = data
        print('Information updated successfully.')
    else:
        print('ID number could not be found. ')
    
def dele():
    IDnum = int(input('Please enter ID number: '))
    if IDnum in my_emp:
        del my_emp[IDnum]
        print('Employee successfully deleted. ')
    else:
        print('ID number could not be found. ')
def save_emp(my_emp):
    out_file = open('Employees.txt', 'wb')
    pickle.dump(my_emp,out_file)
    out_file.close()
    
def display_menu():
    print('1) Look up employee')
    print('2) Add employee')
    print('3) Change employee')
    print('4) Delete employee')
    print('5) Quit program')
main()
