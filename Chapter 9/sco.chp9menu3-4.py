# Chapter IV problems III, IV by Vincenzo Scotto Di Uccio
# The code for the alphabet 
ENCRYPTION = '1'
DECRYPTION ='2'
WORDS = '3'
STOP ='4'
codes = { 'A':'1','B':'2','C':'3','D':'4','F':'5','G':'6','H':'7','I':'8','J':'9','K':'0','L':'11','M':'12','N':'13','O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19','U':'20','V':'21','W':'22','X':'23':'Y':'24','Z':'25'
          ,'a':'50','b':'51','c':'52','d':'53','e':'54','f':'55','g':'56','h':'57','i':'58','j':'59','k':'60','l':'61','m':'62','n':'63','o':'64','p':'65','q':'66','r':'67','s':'68','t':'69','u':'70','v':'71','w':'72','x':'73','y':'74','z':'76'}
def main():
    x = 0
    while x!= STOP:
        valid = 0
        display_menu()

        x = input('Enter your number(1-4): ')
        if x >= '1' and x <= '4':
            if x == ENCRYPTION:
                encry()
            elif x == DECRYPTION:
                decry()
            elif x == WORDS:
                words()
            elif x == STOP:
                return
            else:
                print('Please enter a valid input: ')
    
def encry():
   
    file = open('names.txt','r')
    file2= open('encrypted.txt' , 'w')
    for line in file:
        line = line.rstrip('\n')
        space = ''
        for char in line:
            space += codes[char]
        space += '\n'
        file2.write(space)
    print(' finished')
    
   
    
def decry():
    file = open('encrypted.txt','r')
    dic = {}
    for x in range(len(codes)):
        e , d = codes.popitem()
        dic[d] = e
    for line in file:
        line = line.rstrip('\n')
        space = ''
        for char in line:
            space += dic[char]
        print(space)
        

    
def words():
    unique = set()
    file = open('names.txt','r')
    for line in file:
        line = line.rstrip('\n')
        s = line.split()
        for x in range(len(s)):
            s[x] = s[x].lower()
            s[x] = s[x].strip('.,?!')
        unique.update(s)
    print(unique)

def display_menu():
    print('1) Encryption')
    print('2) Decryption')
    print('3) Unique Words')
    print('4) Stop program')
main()
