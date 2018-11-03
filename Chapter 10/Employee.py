# Employee Class

class employee:
    def __init__(self,name,IDnum,Dep,JobTi):
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
def main():
    e1=employee('Susan Meyers','47899','Accounting','Vice President')
    e2=employee('Mark Jones','39119','IT','Programmer')
    e3=employee('Joy Rodgers','81774','Manufacturing','Engineer')
    print("Name:" ,e1.get_name())
    print("ID Number: ", e1.get_IDnum())
    print("Departemnt: ", e1.get_Dep())
    print("Job Title: ",e1.get_JobTi())

    print("Name:" ,e2.get_name())
    print("ID Number: ", e2.get_IDnum())
    print("Department: ", e2.get_Dep())
    print("Job Title: ",e2.get_JobTi())

    
    print("Name:" ,e3.get_name())
    print("ID Number: ", e3.get_IDnum())
    print("Department: ", e3.get_Dep())
    print("Job Title: ",e3.get_JobTi())
main()
