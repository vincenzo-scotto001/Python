# This problem was asked by Two Sigma.

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) 
# with uniform probability, 
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).
#not sure if I understood the question but I gave it a shot


import math
import random

def rand7():
    rand = random.randint(0,7)
    print(rand)
    if rand <= 5:
        rand5()
    else:
        print('Oh no the number was larger than 5!')

def rand5():
    rand2 = random.randint(0,5)
    print(rand2)

def main():
    answer = input('Wanna Play?(y/n) ')
    
    answer.lower()
    if answer =='n':
        quit()
    else:
        rand7()
main()



