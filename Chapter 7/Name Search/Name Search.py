# Travis Napier
# 10/21/2014
# Name Search

def main():
    # open boy file
    boy_file = open('BoyNames.txt', 'r')
    boy_names = boy_file.readlines()
    #strip \n
    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index = index + 1
    #open girl file
    girl_file = open('GirlNames.txt', 'r')
    girl_names = girl_file.readlines()
    #strip \n
    index = 0
    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n')
        index = index + 1

    #input name
    user_name = input('What is your name? ')
    #search to see if in lists
    
    if user_name in boy_names or user_name in girl_names:
        print('Your name is among the popular.')
    else:
        print('Your name is not among the popular.')

    
    
main()
