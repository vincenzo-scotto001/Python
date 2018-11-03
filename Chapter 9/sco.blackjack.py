from random import choice as rc
def total(hand):

    aces = hand.count(11)


    t = sum(hand)

    if t > 21 and aces > 0:
        while aces > 0 and t > 21:
            # this will switch the ace from 11 to 1
            t -= 10
            aces -= 1
    return t

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


cwin = 0  # computer win counter
pwin = 0  # player win counter
while True:
    player = []
    # draw 2 cards for the player to start
    player.append(rc(cards))
    player.append(rc(cards))
    pbust = False  # player busted flag
    cbust = False  # computer busted flag
    while True:
        # loop for the player's play ...
        tp = total(player)
        print ("The player has these cards %s with a total value of %d" % (player, tp))
        if tp > 21:
            print ("--> The player is busted!")
            pbust = True
            break
        elif tp == 21:
            print ("\a BLACKJACK!!!")
            break
        else:
            hs = input("Hit or Stand/Done (h or s): ").lower()
            if 'h' in hs:
                player.append(rc(cards))
            else:
                break
    while True:
        # loop for the computer's play ...
        comp = []
        comp.append(rc(cards))
        comp.append(rc(cards))
        # dealer generally stands around 17 or 18
        while True:
            tc = total(comp)                
            if tc < 18:
                comp.append(rc(cards))
            else:
                break
        print ("the computer has %s for a total of %d" % (comp, tc))
        # now figure out who won ...
        if tc > 21:
            print ("--> The computer is busted!")
            cbust = True
            if pbust == False:
                print ("The player wins!")
                pwin += 1
        elif tc > tp:
            print ("The computer wins!")
            cwin += 1
        elif tc == tp:
            print ("It's a draw!")
        elif tp > tc:
            if pbust == False:
                print ("The player wins!")
                pwin += 1
            elif cbust == False:
                print ("The computer wins!")
                cwin += 1
        break
    print
    print ("Wins, player = %d  computer = %d" % (pwin, cwin))
    exit = input("Press Enter (q to quit): ").lower()
    if 'q' in exit:
        break
    print
print
print ("Thanks for playing blackjack with the computer!")
