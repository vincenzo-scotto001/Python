# Chapter X problem VIII Trivia game by Vincenzo Scotto Di Uccio
import trivia
def main():
    qst1 = trivia.Trivia("What's my name?","Ty","Travis","Jay","Vincenzo",4)
    qst2 = trivia.Trivia("Where am I from?","New Jersey","New York","New Hampshire","New England",1)
    qst3 = trivia.Trivia("Where was I born?","England","USA","Brazil","Italy",4)
    qst4 = trivia.Trivia("What is the capital of Italy?","Trenton","Rome","Florence","Philly",3)
    qst5 = trivia.Trivia("What is my dog's name?","England","Simbah","Rex","Lyon",2)
    qst6 = trivia.Trivia("What is my mom's name?","Ornella","Lisa","Sheri","Wonda",1)
    qst7 = trivia.Trivia("What is my dad's name?","James","Antonio","Brock","Tom",2)
    qst8 = trivia.Trivia("Month of Birth?","July","January","August","February",3)
    qst9 = trivia.Trivia("What day was I born?","12","10","29","1",3)
    qst10 = trivia.Trivia("What year was I born?","2000","1994","1990","1850",2)

    ply1 = 0
    ply2 = 0
    print('Player One')
    print(qst1)
    ply1_ans = int(input('answer: '))
    if ply1_ans == qst1.get_answer():
        print('Correct')
        ply1 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst1.get_answer())

    print(qst2)
    ply1_ans = int(input('answer: '))

    if ply1_ans == qst2.get_answer():
        print('Correct')
        ply1 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst2.get_answer())

    print(qst3)
    ply1_ans = int(input('answer: '))

    if ply1_ans == qst3.get_answer():
        print('Correct')
        ply1 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst3.get_answer())

    print(qst4)
    ply1_ans = int(input('answer: '))

    if ply1_ans == qst4.get_answer():
        print('Correct')
        ply1 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst4.get_answer())

    print(qst5)
    ply1_ans = int(input('answer: '))

    if ply1_ans == qst5.get_answer():
        print('Correct')
        ply1 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst5.get_answer())

    print()
    print('It is now player two turn.')
    print(qst6)
    ply2_ans = int(input('answer: '))

    if ply2_ans == qst6.get_answer():
        print('Correct')
        ply2 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst6.get_answer())

    print(qst7)
    ply2_ans = int(input('answer: '))

    if ply2_ans == qst7.get_answer():
        print('Correct')
        ply2 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst7.get_answer())

    print(qst8)
    ply2_ans = int(input('answer: '))

    if ply2_ans == qst8.get_answer():
        print('Correct')
        ply2 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst8.get_answer())

    print(qst9)
    ply2_ans = int(input('answer: '))

    if ply2_ans == qst9.get_answer():
        print('Correct')
        ply2 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst9.get_answer())

    print(qst10)
    ply2_ans = int(input('answer: '))

    if ply2_ans == qst10.get_answer():
        print('Correct')
        ply2 += 1
    else:
        print('Incorrect')
        print('Correct answer was: ', qst10.get_answer())

    if ply2 > ply1:
        print('Player Two wins !')
    elif ply1 > ply2:
        print('Player One wins!')
    else:
        print('Tie!')
main()
