# Chapter IV problem I bug collector by Vincenzo Scotto Di Uccio

def main():
        total = 0

        for days in range(1 , 8):
            print("Day", days)
            bugs =int(input("How many bugs did you collect today: "))
            total = total + bugs
        print(" The total amount of bugs you collected is: ", total)
        print ( " Good job!")
main()
