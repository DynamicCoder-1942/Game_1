import random

print("The Stone Paper Scissor Game\n"
      "\n"
      "\n")

print("Rules ::\n"
      "a. Enter 1 for Stone, 2 for Paper, 3 for Scissor.\n"
      "b. Five Rounds in total.\n"
      "\n"
      "\n")

user_inp = input("Enter C to play with Computer and P to play with another Player ----> ")

"""
b= "Stone"
c= "Paper"
d = "Scissor"
"""
if user_inp == "c" or user_inp == "C":
    print("Your are now playing with Computer ::\n")

    comp_pt = 0
    player_pt = 0
    i = 1
    while i < 6:

        a = random.randint(1, 3)

        user_inp1 = int(input("Enter your move :: "))

        if user_inp1 == 1:
            print("You played :: Stone")
        elif user_inp1 == 2:
            print("You played :: Paper")
        elif user_inp1 == 3:
            print("You played :: Scissor")

        if a == 1:
            print("Computer played :: Stone")
        elif a == 2:
            print("Computer played :: Paper")
        elif a == 3:
            print("Computer played :: Scissor")

        if user_inp1 == 1 and a == 1:
            print("Its A TIE.(No one gets point.)")
        elif user_inp1 == 1 and a == 2:
            print("Computer gets a point.")
            comp_pt += 1
        elif user_inp1 == 1 and a == 3:
            print("You get a point.")
            player_pt += 1

        elif user_inp1 == 2 and a == 2:
            print("Its A TIE.(No one gets point.)")
        elif user_inp1 == 2 and a == 3:
            print("Computer gets a point.")
            comp_pt += 1
        elif user_inp1 == 2 and a == 1:
            print("You get a point.")
            player_pt += 1

        elif user_inp1 == 3 and a == 3:
            print("Its A TIE.(No one gets point.)")
        elif user_inp1 == 3 and a == 2:
            print("Computer gets a point.")
            comp_pt = comp_pt + 1
        elif user_inp1 == 3 and a == 1:
            print("You get a point.")
            player_pt = player_pt + 1

        i = i + 1

    print("Result :: ")
    comp_score = comp_pt
    player_score = player_pt

    print(f"Computer Score is {comp_score}\n"
          f"Your Score is {player_score}\n")

    if comp_pt > player_pt:
        print("You lost.")
    else:
        print("Congrats you have won the Game")

elif user_inp == "p" or user_inp == "P":
    print("You are now playing Multi-player ::")

    player_1 = input("Enter Your name Player 1 :: ")
    print(f"Player 1 is {player_1.capitalize()}")
    player_2 = input("Enter Your name Player 2 :: ")
    print(f"Player 2 is {player_2.capitalize()}")

    print("\n")

    play_1_pt = 0
    play_2_pt = 0
    x = 1
    while x < 6:

        play_1_move = int(input(f"Enter you move {player_1.capitalize()} : "))

        play_2_move = int(input(f"Enter you move {player_2.capitalize()} : "))

        if play_1_move == 1 and play_2_move == 1:
            print("TIE.No one gets point.")
        elif play_1_move == 2 and play_2_move == 2:
            print("TIE.No one gets point.")
        elif play_1_move == 3 and play_2_move == 3:
            print("TIE.No one gets point.")

        elif play_1_move == 1 and play_2_move == 2:
            print(f"{player_2.capitalize()} gets a point")
            play_2_pt = play_2_pt + 1
        elif play_1_move == 1 and play_2_move == 3:
            print(f"{player_1.capitalize()} gets a point")
            play_1_pt = play_1_pt + 1

        elif play_1_move == 2 and play_2_move == 3:
            print(f"{player_2.capitalize()} gets a point")
            play_2_pt = play_2_pt + 1
        elif play_1_move == 2 and play_2_move == 1:
            print(f"{player_1.capitalize()} gets a point")
            play_1_pt = play_1_pt + 1

        elif play_1_move == 3 and play_2_move == 1:
            print(f"{player_2.capitalize()} gets a point")
            play_2_pt = play_2_pt + 1
        elif play_1_move == 3 and play_2_move == 2:
            print(f"{player_1.capitalize()} gets a point")
            play_1_pt = play_1_pt + 1

        x = x + 1

    play1_score = play_1_pt
    play2_score = play_2_pt

    print("\n")

    print(f"{player_1.capitalize()} scored :: ", play1_score)
    print(f"{player_2.capitalize()} scored :: ", play2_score)

    print("\n")

    if play1_score > play2_score:
        print(f"{player_1.capitalize()} wins the Game")
    elif play1_score < play2_score:
        print(f"{player_2.capitalize()} wins the Game")

else:
    print("___Invalid Input___")

print("\n"
      "\n")

print("Visit Again....\n"
      "Game Created by Aditya Phadtare.\n"
      "Thank You.")
