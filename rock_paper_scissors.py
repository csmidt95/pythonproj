#Rock paper scisors
import random
from time import sleep
outcomes = ["rock", "paper", "scissors"]

message = {"tie" : "Yawn it's a tie!",
          "won" : "Yay! you won!",
          "lost" : "Awww, you lost"}


def rock_p_s():
    print("Hello, welcome to Rock, Paper, Scissors!")
    sleep(2)
    player_choice = input("""Choose rock, paper, or scissors """)
    player_choice = player_choice.lower()
    computer_choice = random.choice(outcomes)
    print("Okay, here we go!")
    sleep(2)
    print("Rock...")
    sleep(2)
    print("Paper...")
    sleep(2)
    print("Scissors...")
    sleep(2)
    print("SHOOT")
    sleep(1)
    if player_choice == computer_choice:
        print(message["tie"])
        sleep(2)
        responce = input("Play again? " )
        responce.lower()
        if responce == "y" or responce == "yes":
            rock_p_s()
        else:
            print("Have a nice day, whimp!")
        
    elif player_choice == "rock" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "rock" or player_choice == "scissors" and computer_choice == "paper":  
        print(message["won"])
        sleep(2)
        responce = input("Play again? " )
        responce.lower()
        if responce == "y" or responce == "yes":
            rock_p_s()
        else:
            print("Have a nice day, quitter! ")
    else:
        print(message["lost"])
        sleep(2)
        responce = input("Play again? " )
        responce.lower()
        if responce == "y" or  responce == "yes":
            rock_p_s()
        else:
            print("Have a nice day, looser!")
               
rock_p_s()   