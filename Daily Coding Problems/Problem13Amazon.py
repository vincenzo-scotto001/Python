# Given an integer k and a string s, 
# find the length of the longest substring that contains at most k distinct characters.

# For example, 
# given s = "abcba" and k = 2, 
# the longest substring with k distinct characters is "bcb".


#first I will be asking the user for input
amazon = input('Please give me a string: ')
k = int(input('Please give me an integer: '))

#for ease I will be putting the length of the string into a variable
length = len(amazon)


def amazon1(string, integer):

    #need a counter 
    count = 0

    #for every i in the range of 1 and the length of the string plus 1
    for i in range(1,length+1):
        
        # for every j in the range of i
        for j in range(i):

            #if the length of the unique characters in the string from starting index j
            # to the length of the of the string minus i plus j plus 1 is less than or equal to the k integer given
            if len(set(amazon[j:length-i+j+1])) <= k:
                
                #the substring with the maximum distinct values has been found so the substring is equal to the above
                substring = amazon[j:length-i+j+1]

                #increase the count to one
                count = 1
                break
            #breaks the for loop    
            if count == 1:
                break

    #prints the substring
    print(f'substring: {substring}')



amazon1(amazon,k)