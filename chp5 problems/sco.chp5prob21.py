# Chapter V problem XXI rock paper scissors by Vincenzo Scotto Di Uccio

import random

def main():
        x = random.randint(1,3)
        if x == 1:
                x = "Rock"
        elif x==2:
                x = "Paper"
        elif x==3:
                x = "Scissor"

        guess = input("Rock, paper or scissors?: ")
        print("CPU: ",x,"Player: ", guess)
        result = winner(x,guess)
        if result == "tie":
                print("It is a tie, please try again.")
                main()
        else:
            print(result,"Wins!")

def winner(x,guess):
    if guess == "scissors" and x == "rock":
        win = "rock"
        return win
    elif guess == "paper" and x == "scissors":
        win = "scissors"
        return win
    elif guess == "paper" and x == "rock":
        win = "paper"
        return win
    elif guess == "rock" and x == "paper":
        win ="paper"
        return win
    elif guess == "rock" and x == "scissors":
        win = "rock"
        return win
    else:
        win = "tie"
        return win

main()
