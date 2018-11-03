# Class for people
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
