#Chapter IV blackjack by Vincenzo Scotto Di Uccio

def main():
   

    keep_going= 'y'
    score=[]
    num_cards=0
    num_players=0
    high_score=0
    winning_player=[]

   
    deck=create_deck()

   
    num_players=int(input("How many people are playing? "))
    for n in range (num_players):
        score.append(0)
     
    while keep_going=='y':
        num_cards= int(input("How many cards are being dealt? "))
        keep_going,score,deck=deal_cards(deck,num_cards,score,num_players)

  
    player_idx=0
     
    for num in score:
        player_idx+=1
        print("Value of the players %d hand is %d: " %(player_idx, num))
        
        if num > high_score:
            high_score= num
            winning_player.clear()
            winning_player.append(player_idx)

        else:
            if num == high_score:
                winning_player.append(player_idx)
  
    if len(winning_player) == 1:
        print("The high score in this game is %d and the winning player is" %high_score,winning_player[0])
    else:
        print("The high score in this game is %d and there are muntiple winners" %high_score,winning_player)



def create_deck():
   
    deck = { 'Ace of Spades': 1, '2 of Spades':2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs':3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs':6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs':9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Dimonds': 1, '2 of Dimonds': 2, '3 of Dimonds':3,
            '4 of Dimonds': 4, '5 of Dimonds': 5, '6 of Dimonds':6,
            '7 of Dimonds': 7, '8 of Dimonds': 8, '9 of Dimonds':9,
            '10 of Dimonds': 10, 'Jack of Dimonds': 10,
            'Queen of Dimonds': 10, 'King of Dimonds': 10,}
  
    return deck


def deal_cards(deck,num_cards,scores, players):
    
   
    if num_cards > len(deck):
        num_cards=len(deck)
    player_idx=0

  
    while player_idx <= players-1:
        
        
        for count in range(num_cards):
            card, value= deck.popitem()
            print(card,value)
            scores[player_idx] +=value

            if len(deck)==0:
                player_idx=99
                break
        player_idx+=1
    player_idx =1
   
    for num in scores:
        print("Vlaue of the player %d hand is %d: " %(player_idx, num))
        player_idx+=1
   
    if len(deck)>players:
        keep_going= input("Play again? Y/N: ")

    else:
        keep_going='n'
    return (keep_going.lower(),scores,deck)

main()


    
        
