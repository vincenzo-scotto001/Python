# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.




def perfect_number():
    micro = int(input("Please give me a positive integer: "))
    if micro > 0:
    
        for i in range(0,10):
            if micro + i == 10:
                print(f'{micro}{i} gives you a perfect number because they add up to ten.')
    else:
        print('You did not give me a positive integer, try again.')
        perfect_number()



def main():
    answer = input('Wanna Play?(y/n) ')
    
    answer.lower()
    if answer =='n':
        quit()
    else:
        perfect_number()



main()