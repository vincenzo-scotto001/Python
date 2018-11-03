#Sum of Numbers - by Cindy Ireland
# program accepts a positive integer and validates the input and
# prints back the number
def main():
    
    print ('Echo of Numbers after validation by Cindy Ireland')

    theInput = input("Enter a numeric value greater than or = to zero: ")

    theInput = input_validator(theInput)
                                                                
    print ('The number entered is: ', theInput)

def input_validator(aString):

    valueSwitch = 0
    errorSwitch = 0
    make_a_float = 0

    while valueSwitch == 0:
        errorSwitch = 0
        for aChar in aString:

            if (aChar >= '0' and aChar <= '9'):
                errorSwitch = 0
            elif aChar == '.':
                make_a_float = 1
                
            else:
                errorSwitch = 1
                break
        #end of for loop


        if errorSwitch > 0:     
            aString = input('ERROR! Enter a numeric value greater than or = to zero: ')                 
            errorSwitch = 0
        else:
            valueSwitch = 1
    if make_a_float == 1:
        return float(aString)
    else:
        return int(aString)                                     

# your program will actually start here.                       
main()
    

