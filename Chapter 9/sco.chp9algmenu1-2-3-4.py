# Chapter IX menu driven program of algorithm workbench I,II,III,IV by VIncenzo Scotto Di Uccio

WORK_1 = '1'
WORK_2 = '2'
WORK_3 = '3'
WORK_4 = '4'
QUIT = '5'


def main():
    x = 0
    while x!= QUIT:
        valid = 0
        display_menu()

        x = input('Enter your number(1-5): ')
        if x >= '1' and x <= '5':
            if x == WORK_1:
                work_1()
            elif x == WORK_2:
                work_2()
            elif x == WORK_3:
                work_3()
            elif x == WORK_4:
                work_4()
            elif x == QUIT:
                return
            else:
                print('Please enter a valid input: ')
def work_1():
    d = {'a':1,'b':2,'c':3}
    print('The dictionary is: ', d)
    print(' The first value is: ' , d['a'])
    print(' The second value is: ' ,d['b'])
    print('The third value is: ', d['c'])
    print(' The keys are: ' ,d.keys())
        

def work_2():
    d = {}
    d2 = dict()
    print(' d is a :',type(d), 'it has a length of: ', len(d))
    print(' d2 is a :',type(d2), 'it has a length of: ', len(d2))
def work_3():
    # I renamed the file 
    file = open('names.txt', 'r')
    infile = file.readline()
    dct = {}
    index =0
    for file in infile:
        file = file.rstrip('\n')
        dct[index]= file
        index +=1 
    if 'james' in dct:
        print ("Yes the name is in the file.")
    else:
        print('Sorry the name is not in the file.')
def work_4():
    
    file= open('names.txt','r')
    infile = file.readlines()
    dct={}
    index = 0
    index1=0
    for file in infile:
        file = file.rstrip('\n')
        dct[index] = file
        index += 1
    print(dct)
    for x in range(len(dct)):
        if dct[index1] =='John Locke':
            del dct[index1]
            index1 +=1
            
        else:
            print(' His name is not in the dictionary.')
    print(dct)
        
    
    

def display_menu():
    print("1) Workbench 1 ")
    print("2) Workbench 2 ")
    print("3) Workbench 3")
    print("4) Workbench 4")
    print('5) Quit')
    
main()

    
