# Blackjack program by Vincenzo Scotto Di Uccio
while again == 'y':
    num_cards = int(input('How many cards are dealt: '))
    again,score,deck = deal_cards(deck,num_cards,score,num_players)
                    



player_idx = 0
for num in score:
    player_idx+=1
    print ('Value of the player is %d hand is %d: ', %(player_idx,num))
    if num > high_score:
        high_score = num
        winning.player.clear()
        winning_player.append(player_idx)
    else:
        if num == high score:
        
