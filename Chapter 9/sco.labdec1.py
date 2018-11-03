# Lab for december 1st by Vincenzo Scotto Di Uccio


PRO_1='1'
PRO_2='2'
QUIT='3'
space=''


class Personal:
    def __init__(self,name,address,age,phone):
        print(space)
        self.__name=name
        self.__address=address
        self.__age=age
        self.__phone=phone

    def set_name(self,name):
        self.__name=name
    def set_addredd(self, address):
        self.__address=address  
    def set_age(self,age):
        self.__age=age  
    def set_phone(self,phone):
        self.__phone=phone  
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone
    def __str__(self):
        return "Name: "+self.__name+\
               "\nAddress:"+self.__address+\
               "\nAge:"+self.__age+\
              "\nPhone:"+self.__phone

  
class employee:
    def __init__(self,name,IDnum,Dep,JobTi):
        print(space)
        self.__name=name
        self.__IDnum=IDnum
        self.__Dep=Dep
        self.__JobTi=JobTi


    def set_name(self,name):
        self.__name=name
    def set_IDnum(self, IDnum):
        self.__IDnum=IDnum  
    def set_Dep(self,Dep):
        self.__Dep=Dep  
    def set_JobTi(self,JobTi):
        self.__JobTi=JobTi  
    def get_name(self):
        return self.__name
    def get_IDnum(self):
        return self.__IDnum
    def get_Dep(self):
        return self.__Dep
    def get_JobTi(self):
        return self.__JobTi
    def __str__(self):
        return "Name: "+self.__name+\
               "\nAddress:"+self.__IDnum+\
               "\nAge:"+self.__age+\
              "\nPhone:"+self.__phone
#def main 
def main():
   
    choice =0
    
    while choice!=QUIT:
        display_menu()
 
        choice=input("Please enter a choice 1-3:")
        if (choice>='1' and choice<='3'):
            if choice ==PRO_1:
                pro_1()
            elif choice==PRO_2:
                pro_2()
            else:
                print("The program in ending, good day!")
 
def pro_1():
    
    name=('Vincenzo')
    address=('2088 Florence Avenue,NJ')
    age=('21')
    phone=('(732)-284-7491')
    info=Personal(name,address,age,phone)
    print("Name:" ,info.get_name())
    print("Address: ", info.get_address())
    print("Age: ", info.get_age())
    print("Phone Number: ",info.get_phone())
 
    two()
    
def two():
    name=('Matt')
    address=('1315 College Avenue,PA')
    age=('21')
    phone=('(901)-555-1758')
    info=Personal(name,address,age,phone)
    print("Name:" ,info.get_name())
    print("Address: ", info.get_address())
    print("Age: ", info.get_age())
    print("Phone Number: ",info.get_phone())

    three()
def three():
    name=('Luigi')
    address=('1000 Main Street, NJ')
    age=('19')
    phone=('(895)-465-6565')
    info=Personal(name,address,age,phone)
    print("Name:" ,info.get_name())
    print("Address: ", info.get_address())
    print("Age: ", info.get_age())
    print("Phone Number: ",info.get_phone())
    print(space)

 
def pro_2():
    name=('Susan Meyers')
    IDnum=('47899')
    Dep=('Accounting')
    JobTi=('Vice President')
    info=employee(name,IDnum,Dep,JobTi)
    print("Name:" ,info.get_name())
    print("ID Number: ", info.get_IDnum())
    print("Departemnt: ", info.get_Dep())
    print("Job Title: ",info.get_JobTi())

    x()
    
def x():
    name=('Mark Jones')
    IDnum=('39119')
    Dep=('IT')
    JobTi=('Programmer')
    info=employee(name,IDnum,Dep,JobTi)
    print("Name:" ,info.get_name())
    print("ID Number: ", info.get_IDnum())
    print("Department: ", info.get_Dep())
    print("Job Title: ",info.get_JobTi())

    y()
def y():
    name=('Joy Rogers')
    IDnum=('81774')
    Dep=('Menufacturing')
    JobTi=('Engineer')
    info=employee(name,IDnum,Dep,JobTi)
    print("Name:" ,info.get_name())
    print("ID Number: ", info.get_IDnum())
    print("Department: ", info.get_Dep())
    print("Job Title: ",info.get_JobTi())
    print(space)
 
    
def display_menu():
    print("1) Personal ")
    print("2) Employee")
    print("3) QUIT!")
 
main()
