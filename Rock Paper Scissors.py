import random
def get_choices():
    player_choice=input("Enter choice ROCK , PAPER OR SCISSORS: ")
    choose=['ROCK','PAPER','SCISSORS']
    computer_choice=random.choice(choose)
    choice={"player":player_choice,"computer":computer_choice}
    return choice


def check_win(player,computer):
    print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
    if player==computer:
        return "It's a tie!"
    elif player=="ROCK" :
        if computer=="SCISSORS":
            return "ROCK SMASHES SCISSORS! YOU WIN!"
        else:
            return "PAPER COVERS ROCK! YOU LOSE!"
    elif player=="PAPER" :
        if computer=="ROCK":
            return "PAPER COVERS ROCK! YOU WIN!"
        else:
            return "SCISSORS CUT PAPER! YOU LOSE!"
    elif player=="SCISSIORS" :
        if computer=="ROCK":
            return "ROCK SMASHES SCISSORS! YOU LOSE!"
        else:
            return "SCISSORS CUT PAPER! YOU WIN!"

choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)