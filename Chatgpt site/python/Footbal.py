import random

User_points = 0
Computer_points = 0

def main():
    while True:
        welcome = input("Welcome to Python Football! Would you like to play? (y/n) ")
        if welcome == ("y"):
            break
        elif welcome == ("n"):
            exit()
        else:
            print("Please enter a valid response.")
        
        

main()
def game():
    team_name = input("Please enter your team name: ")
    print("Welcome", team_name)
    print(team_name, "v.s. Pythons")

game() 