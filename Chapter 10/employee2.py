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
    def get_JobTi(self):
        return self.__Job
    
