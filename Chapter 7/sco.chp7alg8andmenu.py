# Menu driven program for November 10th by Vincenzo Scotto Di Uccio
import random
TWO_D = '1'
MIN_MAX = '2'
LIST_A_B = '3'
RANDOM = '4'
QUIT ='5'

def main():
    
    x = 0

    while x != QUIT:
        valid = 0
        display_menu()

        x = input(" Enter your number(1-5): ")

        if x >= "1" and x <= "4":
            if x == TWO_D:
                two_d()
            elif x == MIN_MAX:
                min_max()
            elif x == LIST_A_B:
                list_a_b()
            elif x == RANDOM:
                random1()
            elif x == QUIT:
                return
            else:
                print(" Please enter a valid input(1,2,3,4,5): ")



def two_d():
    ROWS = 5
    COL = 3

    values = [[0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0],
              [0,0,0]]
    for r in range(ROWS):
        for c in range(COL):
            values[r][c] = int(input(' Please give me a number: '))
    print (' The list you created is: ' ,values)
def min_max():
    x =int(input(" Please enter a range: "))
    list1=[]

    for i in range(x):
        list1.append(random.randint(0,100))
    list1.sort()
    print('The minimum value is: ',list1[0])
    print('The max value is: ', list1[-1])
def list_a_b():
    list_a =[1,2,3]
    list_b =[]
    list_b = list_a
    print('list a is: ' ,list_a)
    print('list b is: ' ,list_b)
    if list_a is list_b:
        print('True')
    else:
        print('False')
    list_c = [4,5,6]
    list_b = list_c
    print('List b is now: ', list_b)
    print('List a is still: ', list_a)
    if list_a is list_b:
        print('True')
    else:
        print('False')
    
def random1():
    list1= []
    list2= {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    for i in range(5):
        list1.append(random.randint(0,26))
    for x in list1:
        print(list2[x])
    list1.sort()
    tuple1 = tuple(list1)
    tuple2=tuple(list2)
    print('The random numbers: ' ,tuple1)        
    
        
    
    
    
            
def display_menu():
    print('1) Two-Dimensional list')
    print('2) Min Max')
    print('3) List A and B')
    print('4) Random')
    print('5) Quit')
    
main()
