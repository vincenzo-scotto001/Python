# Chpater VIII problem XII pig latin by Vincenzo Scotto Di Uccio 
def main():
    #input sentence
    sentence = input('Input a sentence: ')
    #list the sentence
    sent_list = sentence.split()
    # print end of word, add first letter to end, add ay
    index = 0
    print('Translation: ')
    while index < len(sent_list):
        print(sent_list[index][1:].upper() + sent_list[index][0].upper() + 'AY ', end = '')
        index = index + 1


    
main()
