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
