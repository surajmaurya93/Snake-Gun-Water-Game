import random

print("welcome to rock paper sissor game")

def RPS():  
  player_input = input("Enter your choice (rock, paper, sissor): ")
  comuter_choice = random.choice(["rock", "paper", "sissor"])
  
  print(f"you choose {player_input} and computer choose {comuter_choice}")
  
  if player_input == comuter_choice:
    print("the game is draw")
  elif player_input == "rock" and comuter_choice == "sissor":
    print("you won the game")
  elif player_input == "paper" and comuter_choice == "rock":
    print("you won the game")
  elif player_input == "sissor" and comuter_choice == "paper":
    print("you won the game")
  else:
    print("you lost the game")

while True:
    print("\n1. Start the game")
    print("2. Exit the game")
    choice=int(input("Enter your choice : "))
    if choice==1:
        RPS()
    if choice==2:
        break


