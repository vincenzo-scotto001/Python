# Implement an autocomplete system. 
# That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

# For example, 
# given the query string de and the set of strings [dog, deer, deal], return [deer, deal].


test = ['dog', 'deer', 'deal'] #create the sample list of strings
query = 'de' # create the queue
twitter = list(query.split(' ')) #convert to list for convience
matches = [] #create empty list


#takes in 3 parameters , looks at the queue and sees if the len of the queue matches with any of the strings and appends them in the list called matches
def twitters(test,twitter,matches):
    for c in test:
        if c[0:len(twitter)+1] == twitter[0]:
        #print(''.join(list(c[:])))
            matches.append(''.join(list(c[:])))
    return matches


twitters(test,twitter,matches)

