# Chapter X problems III,IV by Vincenzo Scotto Di Uccio
 
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

    

    def __str__(self):
        return ('The name is %s, the address is %s, the age is %s, and number is %s' \
                %(self.__name,self.__address,self.__age,self.__phone))


  
class employee:
    def __init__(self,name,IDnum,Dep,JobTi):
        print(space)
        self.__name=name
        self.__IDnum=IDnum
        self.__Dep=Dep
        self.__JobTi=JobTi

    def __str__(self):
        return ('The name is %s, the ID is %s, the Dept. is %s, and Job Title is %s' \
                %(self.__name,self.__IDnum,self.__Dep,self.__JobTi))
 
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
    
    g=Personal('Vincenzo', '2088 Florence Avenue,NJ','21','732-284-7491')
    b=Personal('Matt', '1315 College Avenue,PA', '21','888-555-9595')
    c=Personal('Luigi', '1000 Main Street','19','865-555-6948')
    
    print(g)
    print(b)
    print(c)

 
def pro_2():
    s=employee('Susan Meyers','47899','Accounting','Vice President')
    m=employee('Mark Jones', '39119','IT','Programer')
    j=employee('Joy Rogers','81774','Manufacturing','Engineer')
    
    print(s)
    print(m)
    print(j)


 
    
def display_menu():
    print("1) Personal")
    print("2) Employee")
    print("3) QUIT!")
 
main()
