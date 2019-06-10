# Implement a job scheduler which takes in a 
# function f and an integer n, 
# and calls f after n milliseconds.


import time
from threading import Timer

print('Time: ', time.time())


def f():
    print('hello world')


n = 1000000 #this is in seconds 

def timer(f,n):
    print(time.time())
    time.sleep(n/10000) #converts to mili
    f()
    print(time.time())


timer(f,n)



    