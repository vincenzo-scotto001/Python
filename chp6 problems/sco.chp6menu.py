# Menu driven program/ file processing by Vincenzo Scotto Di Uccio

FILE_HEAD_DISP = "1"
ITEM_COUNT = "2"
STOP = "3"

def main():

    x = 0
    while x != STOP:
        valid = 0
        display_menu()

        x = input( "Enter your number(1-3): ")
        if x >="1" and x <= "5":
            if x == FILE_HEAD_DISP:
                file_head()
            elif x == ITEM_COUNT:
                item_count()
            else:
                print(" ERROR, please type a valid input(1,3): ")
def file_head():
    line = 0
    
    infile = input("Enter the name of the file here: ")
    file = open(infile,"r")
    for line in (1,6):
        line1 = file.readline()
        print(line1)
        
    file.close()
        
    

def item_count():
    t = 0

    try:
        file =open("numbers.txt","r")
        for line in file:
            amount = float(line)
            t += amount
            file.close()
            print ("The total is: ", t)
    except:
        print("Error")

def display_menu():
    print (" 1) file head display ")
    print (" 2) item count ")
    print (" 3) stop program" )



main()

