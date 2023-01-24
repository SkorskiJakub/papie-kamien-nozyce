import random

def user_choice():
    user_input = int(input("\nPlease choose. Number 1 to play with another player or number 0 to play with computer: "))
    if user_input == 1:
        print("Great. We're starting the game. Your oponent is second player")
        start_game_player()
    elif user_input == 0:
        print("Great. We're starting the game. Your oponent is computer.")
        start_game_comp()
    else:
        print("You made a mistake. please try again")
        user_choice()
        
def start_game_comp():
    user1_game = int(input("\nPlease choose: 1 is Scissor; 2 is Rock; 3 is Paper: "))
    if user1_game == 1:
        print("\nYour choice is Scissor")
    elif user1_game == 2:
        print("\nYour choice is Rock")
    elif user1_game == 3:
        print("\nYour choice is Paper")
    else:
        print("\nYou made a mistake.")
        start_game_comp()

    comp_game = random.randint(1, 3)
    if comp_game == 1:
        print("Computer choice Scissor")
    elif comp_game == 2:
        print("Computer choice Rock")
    else:
        print("Computer choice Paper")

    print("\nLets check who will win")

    if user1_game == comp_game:
        print("No winner. Try again")
    elif (user1_game == 1 and comp_game) == 3 or (user1_game == 3 and comp_game == 2) or (user1_game == 2 and comp_game == 1):
        print("You win. Congratulations")
    else:
        print("Computer win. You don't have enought lucky at this time")

    user_cont = input("\nWould you like to try again? Please choose 'y' for yes and 'n' for no: ").lower()
    if user_cont == 'y':
        user_choice()
    elif user_cont == 'n':
        print("Thank you. See you soon.")
    else:
        print("Your answer is not correct. I have to finish your game")


def start_game_player():
    user1_game = int(input("\nPlayer 1. \nPlease choose: 1 is Scissor; 2 is Rock; 3 is Paper: "))
    user2_game = int(input("\nPlayer 2. \nPlease choose: 1 is Scissor; 2 is Rock; 3 is Paper: "))
    if user1_game == 1:
        print("\nPlayer 1 choice is Scissor")
    elif user1_game == 2:
        print("\nPlayer 1 choice is Rock")
    elif user1_game == 3:
        print("\nPlayer 1 choice is Paper")
    else:
        print("\nPlayer 1 made a mistake.")
        start_game_player()

    if user2_game == 1:
       print("\nPlayer 2 choice is Scissor")
    elif user2_game == 2:
        print("\nPlayer 2 choice is Rock")
    elif user2_game == 3:
        print("\nPlayer 2 choice is Paper")
    else:
        print("\nPlayer2 made a mistake.")
        start_game_player()

    print("\nLets check who will win")

    if user1_game == user2_game:
        print("No winner. Try again")
    elif (user1_game == 1 and user2_game) == 3 or (user1_game == 3 and user2_game == 2) or (user1_game == 2 and user2_game == 1):
        print("Player 1 win. Congratulations")
    else:
        print("Player 2 win. Congratulations")

    user_cont = input("\nWould you like to try again? Please choose 'y' for yes and 'n' for no: ").lower()
    if user_cont == 'y':
        user_choice()
    elif user_cont == 'n':
        print("Thank you. See you soon.")
    else:
        print("Your answer is not correct. I have to finish your game")
        
print("Hello, we start a game -> Paper / Scissor / Rock.")
user_choice()
