import random

player_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("""
    __- Welcome to Rock, Paper, Scissors -__
    
    [Type Rock, Paper, Scissors, or Q to quit]: """)
    if user_input == ("q"):
        print()
        print("""________________________________________________________

        __- You have quit the game -__
        """)
        break
    elif user_input not in options:
        print("""________________________________________________________
        """)
        print("Please enter a valid selection")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("""________________________________________________________

    Computer Picked""", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("""    
        Victory""")
        player_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("""   
        Victory""")
        player_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("""    
        Victory""")
        player_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("""
        Tie""")
        ties += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("""
        Tie""")
        ties += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("""
        Tie""")
        ties += 1

    else:
        print("""    
        Defeat""")
        computer_wins += 1
    
    print ("________________________________________________________")
    
amount = ("times")
print()
if player_wins == 1:
    amount = ("time")
player_scoreboard = print("    - You have won", (player_wins), amount)
print()

amount = ("times")

if computer_wins == 1:
    amount = ("time")
computer_scoreboard = print("    - The Computer has won", (computer_wins), amount)
print()
   
amount = ("times")

if ties == 1:
    amount = ("time")
tie_scoreboard = print("    - You have tied", (ties), amount)

input()

#rock 0 paper 1 scissors 2        

print("    Goodbye!")

