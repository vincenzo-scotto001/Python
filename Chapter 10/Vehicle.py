# Chapter X problem II by Vincenzo Scotto Di Uccio

class Vehicle:
    def __init__(self,year,make):
        self.__year_model=year
        self.__make=make
        self.__speed=0
    
    def accel(self):
        self.__speed +=5

    def brake(self):
        self.__speed-=5

    def get_speed(self):
        return self.__speed
