# Chapter IV workbench IX by Vincenzo Scotto Di Uccio


def main():
        x = "y"

        t = 0

        while x == "y":
            
            
          
            n = int(input(" Enter a number between 1 to 100 please: "))

        
            while n < 1 or n > 100:
                    print (" Someone cannot follow rules correctly, I like that.")
                    n =int(input("Try again: "))
        
            t = t + n
            print(" Yay! That number is in the range!")
            print (" The total is: ", t)
           


main()
