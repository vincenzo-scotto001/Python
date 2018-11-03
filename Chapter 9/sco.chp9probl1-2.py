# Chapter IX problems I, II in menu by vincenzo scotto di uccio

COURSE = '1'
CAPITAL = '2'
STOP = '3'
import random
def main():
    x = 0
    while x != STOP:
        valid = 0
        display_menu()

        x = input('Enter your number please(1-3): ')

        if x >= '1' and x<= '3':
            if x == COURSE:
                course()
            elif x == CAPITAL:
                capital()
            elif x == STOP:
                return
            else:
                print("Enter a valid input: ")

def course():
    dct1={'CS101':'3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244','CM241':'1411'}
    dct2={'CS101': 'Haynes','CS102':'Alvarado','CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    dct3={'CS101':'8:00 AM','CS102':'9:00 AM','CS103':'10:00 AM','NT110':'11:00 AM','CM241':'1:00 PM'}
    x = input('Please enter the course number: ')
    if x == 'CS101':
        print(' The details for this class are: ', 'room number:',dct1['CS101'],'professor: ',dct2['CS101'],'time: ',dct3['CS101'])
    elif x == 'CS102':
        print(' The details for this class are: ', 'room number:',dct1['CS102'],'professor: ',dct2['CS102'],'time: ',dct3['CS102'])
    elif x == 'CS103':
        print(' The details for this class are: ', 'room number:',dct1['CS103'],'professor: ',dct2['CS103'],'time: ',dct3['CS103'])
    elif x == 'NT110':
        print(' The details for this class are: ', 'room number:',dct1['NT110'],'professor: ',dct2['NT110'],'time: ',dct3['NT110'])
    elif x == 'CM241':
        print(' The details for this class are: ', 'room number:',dct1['CM241'],'professor: ',dct2['CM241'],'time: ',dct3['CM241'])
    else:
        print('Please enter a correct number. ')

def capital():
    capitals={"Washington":"Olympia","Oregon":"Salem",\
                    "California":"Sacramento","Ohio":"Columbus",\
                    "Nebraska":"Lincoln","Colorado":"Denver",\
                    "Michigan":"Lansing","Massachusetts":"Boston",\
                    "Florida":"Tallahassee","Texas":"Austin",\
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                    "Alaska":"Juneau","Utah":"Salt Lake City",\
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                    "South Dakota":"Pierre","West Virginia":"Charleston",\
                    "Virginia":"Richmond","New Jersey":"Trenton",\
                    "Minnesota":"Saint Paul","Illinois":"Springfield",\
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                    "Tennessee":"Nashville","Georgia":"Atlanta",\
                    "Alabama":"Montgomery","Mississippi":"Jackson",\
                    "North Carolina":"Raleigh","South Carolina":"Columbia",\
                    "Maine":"Augusta","Vermont":"Montpelier",\
                    "New Hampshire":"Concord","Connecticut":"Hartford",\
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                    "Montana":"Helena","Kansas":"Topeka",\
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                    "Maryland":"Annapolis","Missouri":"Jefferson City",\
                    "Arizona":"Phoenix","Nevada":"Carson City",\
                    "New York":"Albany","Wisconsin":"Madison",\
                    "Delaware":"Dover","Idaho":"Boise",\
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

    wrong=[]

    print ("STATE TEST \n")

    incorrect_answers = False

    while len(capitals)>0:
        pick=random.choice(list(capitals.keys()))
        correct_answer=capitals.get(pick)
        print ("What is the capital city of",pick,"?")
        answer=input("Your answer: ")
        if answer.lower()==correct_answer.lower():
            print ("That's Correct!\n")
        else:
            print ("That's Incorrect.")
            print ("The correct answer is",correct_answer)
            wrong.append(pick)
            incorrect_answers = True
    del capitals[pick]

    print ("You missed",len(wrong),"states.\n")


    if incorrect_answers:
        print ("Here are the ones that you may want to brush up on:\n")
        for each in wrong:
            print (each)
    else:
        print ("Perfect!")
    
    
def display_menu():
    print('1) Course')
    print('2) Capital')
    print('3) Stop')
main()
