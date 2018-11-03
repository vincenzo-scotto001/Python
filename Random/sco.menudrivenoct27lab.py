# October 27th 8-2 8-9 8-10 menu driven program

PROB8_2 = "1"
PROB8_9 = "2"
PROB8_10 = "3"
QUIT = "4"

def main():
    x = 0
    while x != QUIT:
        valid = 0
        display_menu()
        
        print()
        x = input( "Enter your number(1-5): ")
        if x >= "" and x <= "5":
            if x == PROB8_2:
                prob8_2()
                
            elif x == PROB8_9:
                prob8_9()
                
            elif x == PROB8_10:
                prob8_10()
                
            elif x == QUIT:
                return
            else:
                print (" Please enter a valid input(1,2,3,4)" )


def prob8_2():
    result = 0
    file = open("numbers.txt", "r+")
    linein = file.readline()
    for s in open("numbers.txt"):
        result += int(s.strip())
    print ("The sum of the numbers is: ", result)

    total = str(result)
    total.split()

    total_total = 0
    for x in total:
        num = int(x)
        total_total += num
    print ("The sum of the digits: " , total_total)
    print()
        
    
    
        

    
    

    
def prob8_9():
    

    file = open("names.txt" ,"r")
    linein = file.readline()
    while linein != '':
        print(" The names: ", linein)
        linein.split()
        v = 0
        c = 0
        for x in linein:
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
                v += 1
            else:
                c += 1
        print (" The amount of vowels is: ", v)
        print (" The amount of consonants is: " ,c)
        linein = file.readline()
        

def prob8_10():
    file = open("names.txt", "r")
    linein = file.read()
    while linein != '':
        print ("The names: ", linein)
        linein.split()
        j = 0
        o = 0
        h = 0
        n = 0
        l = 0
        c = o
        k = 0
        e = 0
        d = 0
        a = 0
        v = 0
        i = 0
        h = 0
        u = 0
        m = 0
        b = 0
        r = 0
        c = 0
        f = 0
        s = 0
        p = 0
        t = 0
        # i had no idea how else to do this, it is very ugly i know
        # and it prints even uglier
        
        for x in linein:
            if x == "j" or x == "J":
                j += 1
            elif x == "o":
                o += 1
            elif x == "h" or x =="H":
                h += 1
            elif x == "n":
                n += 1
            elif x == "l" or x == "L":
                l += 1
            elif x == "c":
                c += 1
            elif x == "k":
                k += 1
            elif x == "e":
                e += 1
            elif x == "d" or x =="D":
                d += 1
            elif x == "a":
                a += 1
            elif x == "v":
                v += 1
            elif x == "i":
                i += 1
            elif x == "u":
                u += 1
            elif x == "m":
                m += 1
            elif x == "b" or x=="B":
                b += 1
            elif x == "r":
                r += 1
            elif x == "c" or x =="C":
                c += 1
            elif x == "f":
                f += 1
            elif x == "s":
                s += 1
            elif x == "p" or x == "P":
                p += 1
            elif x == "t":
                t += 1
                
            print ("The amount of j's: " ,j)
            print ("The amount of o's: " ,o)
            print ("The amount of h's: " ,h)
            print ("The amount of n's: " ,n)
            print ("The amount of l's: " ,l)
            print ("The amount of c's: " ,c)
            print ("The amount of k's: " ,k)
            print ("The amount of e's: " ,e)
            print ("The amount of d's: " ,d)
            print ("The amount of a's: " ,a)
            print ("The amount of v's: " ,v)
            print ("The amount of i's: " ,i)
            print ("The amount of u's: " ,u)
            print ("The amount of m's: " ,m)
            print ("The amount of b's: " ,b)
            print ("The amount of r's: " ,r)
            print ("The amount of c's: " ,c)
            print ("The amount of f's: " ,f)
            print ("The amount of s's: " ,s)
            print ("The amount of p's: " ,p)
            print ("The amount of t's: " ,t)
            linein = file.read()
    


def display_menu():
    print ("MENU")
    print (" 1) Sum of Digits ")
    print (" 2) Vowels and Consonants")
    print (" 3) Most Frequent Character")
    print (" 4) Stop program")



main()
