# Chapter X program VI by Vincenzo Scotto Di Uccio
import pickle
import os.path

class Employee:
    def __init__(self,name,IDnum,Dep,Job):
        self.__name = name
        self.__IDnum = IDnum
        self.__Dep = Dep
        self.__Job = Job
    def set_name(self,name):
        self.__name = name
    def set_IDnum(self,IDnum):
        self.__IDnum = IDnum
    def set_Dep(self,Dep):
        self.__Dep = Dep
    def set_Job(self,Job):
        self.__Job = Job
    def get_name(self):
        return self.__name
    def get_IDnum(self):
        return self.__IDnum
    def get_Dep(self):
        return self.__Dep
    def get_Job(self):
        return self.__Job
    
        
def main():
    ch = 'y'
    if os.path.exists('emp.dat'):
        file = open('emp.dat','rb')
        emp_dict = pickle.load(file)
        file.close()
    else:
        e1 = Employee('Susan Meyers','47899','Accounting','VP')
        e2 = Employee('Mark Jones','37119','IT','Programmer')
        e3 = Employee('Joy Rodgers','81774','Manufacturing','Engineer')
        emp_dict ={e1.get_IDnum():e1.get_name()+''+e1.get_Dep()+''+e1.get_Job()}


    while ch.upper() == 'Y':
        print ('Enter any of the following choices: ')
        print ('1) Look Up')
        print ('2) Enter New')
        print ('3) Change Employee')
        print ('4) Delete Employee')
        print ('5) Quit')

        x = input('Enter your choice: ')
        if int(x) == 1:
            IDnum = input('Enter ID number: ')
            if int(IDnum) in emp_dict.keys():
                print(emp_dict[int(IDnum)])
            else:
                print('Not found')
        
            
        if int(x) == 2:
            IDnum = input('Enter ID number: ')
            if int(IDnum) in emp_dict.keys():
                print('Employee already exists')
            else:
                name = input('Enter name: ')
                Dep = input('Enter Department: ')
                Job = input('Enter Job: ')
                e4 = Employee(name, int(IDnum),Dep,Job)
                emp_dict[e4.get_IDnum()] = e4.get_name()+''+e4.get_Dep()+''+e4.get_Job()
                print('Added')
        if int(x) == 3:
            IDnum = input('Enter ID number: ')
            if int(IDnum) in emp_dict.keys():
                name = input('Enter name: ')
                Dep = input('Enter Department: ')
                Job = input('Enter Job: ')
                e4 = Employee(name, int(IDnum),Dep,Job)
                emp_dict[e4.get_IDnum()] = e4.get_name()+''+e4.get_Dep()+''+e4.get_Job()
                print('Modified')
            else:
                print('Not Found')
        if int(x) ==4:
            IDnum = input('Enter ID number: ')
            print('Deleted', emp_dict.pop(int(IDnum),'Not Found'))
        #if int(x) != 5:
         #   print('Invalid Choice')
        else:
            print('Bye now!')
        
        ch = input('Continue? enter "y" for yes: ')
        file = open('emp.dat','wb')
        pickle.dump(emp_dict,file)
        file.close()
        
            

main()
        
