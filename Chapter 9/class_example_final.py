class Duck:
    def __init__(self,value,name):        #__init__ is the defalut constructor method defined by Python
        print("inside class constructor, which is a default private method for the class")
        self.__v = value             # the .__v syntax make a private variable
        self.name = name                           
        print("construtor method ", " value = ",self.__v)   #the scope of the variable self._v is the class not just the function within the class

        color = "red"               #the scope of the variable color is just the function __init__ because it is not associated with self, which is the object
        print("%s is %s" %(name,color))
    def quack(self):
        print('Quaaack! says %s ' %self.name)   #even though self._v was defined in the function __init__ the scope is the class
    def walk(self):
        print('Object number ', self.__v, 'Walks like a duck.')
        #print('Object number ', self._v, ' is the color ', color)  #uncomment and run color will be undefined to this function
    def __str__(self):
        return ('The duck"s name is %s and their value is %d' %(self.name,self.__v))

def main():
    donald = Duck(47,"Donald")
    donald.quack()
    donald.walk()
    printObject(donald)
    #instanciate (create) a new object; encapsulation
    #different objects can have different values
    huey = Duck(17,"Huey")  #creates a new instance of Duck
    huey.quack()
    huey.walk()
#shallow copy of an existing object
    luey = donald
    if donald is  huey:
        print("Yes, donald and huey are the SAME object")
    else:
        print("No, Donald and Huey are unique duck objects")
    if donald is  luey:
        print("Yes, Donald and Luey are the SAME object \n")
    else:
        print("No, Donald and Luey are unique duck objects \n")
    
    printObject(luey)
    printObject(huey)

    print("Notice the difference between the methods we defined quack and walk and the default methods provided by Python \n")

    luey.name = "Luey"
    printObject(donald)
    printObject(luey)
    
def printObject(theObject):
     print(theObject, " contains these default methods ", dir(theObject))
     print(theObject.__class__, " parent class for object ")
     print(theObject.__dir__, " the dir method for the object \n")
    

main()
