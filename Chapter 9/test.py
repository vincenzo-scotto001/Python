# Chapter IX problems III,IV, by Vincenzo Scotto Di Uccio
# I put my own twist on this, hope you do not mind
CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}','R':'00','r':'21',\
            'S':'01','s':'23','T':'002','t':'003'}
    # Constants for the menu choices
ENCRYPTION = '1'
DECRYPTION ='2'
WORDS = '3'
STOP ='4'

def main():
    x = 0
    while x!= STOP:
        valid = 0
        display_menu()

        x = input('Enter your number(1-4): ')
        if x >= '1' and x <= '4':
            if x == ENCRYPTION:
                encrypt()
            elif x == DECRYPTION:
                decrypt()
            elif x == WORDS:
                words()
            elif x == STOP:
                return
            else:
                print('Please enter a valid input: ')

    # Encryption
def encrypt():

        #Obtain a string of converted text
        result = convert()

        #Open and write in output file
        output_name = input("Enter the name of the output file: ")
        output_file = open(output_name, 'w')
        output_file.write(result)
        output_file.close()

    # Decryption
def decrypt():

        # obtain a string  of converted text
        result = convert()

        # write text to screen
        print(result)

    #The convert function aske the user for a file name, opens the file and converts its contents using the CODE above.
def convert():
        input_name = input("Enter the name of the input file: ")
        input_file = open(input_name, 'r')

        result = ''
        text = input_file.read()

        #Convert all charactors but spaces.
        for ch in text:

            if ch.isspace():
                result = result + ch
            else:
                result = result + CODE[ch]

        return result
def words():
    file = open('names.txt','r')
    infile = file.read()
    words = infile.split()
    file2 = open('words.txt','w')
    unique = set(words)
    for word in words:
        file.write(str(word))
    print (unique)
    
    

def display_menu():
        print(' 1) Encrypt a file')
        print(' 2) Decrypt a file')
        print(' 3) Unique words')
        print(' 4) Exit')

main()
