# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

test = [10,15,3,7]
k = 17

def addfinder(lis,num):
    for i in range(len(lis)):
        for x in range(len(lis)):
            if lis[i]+lis[x] == num:
                print(f'These two numbers add up to k({num}): ', lis[i],lis[x])
            else:
                print('No')

addfinder(test,k)


