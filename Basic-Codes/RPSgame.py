import random

def rpsgame():
    comp_points = 0
    player_points = 0
    sign = [1, 2, 3]
    for i in range(10):
        comp = random.choice(sign)
        print("""\nChoose an Option:
1. Rock
2. Paper
3. Scissor""")
        player = int(input("Select between 1 to 3 : "))
        if comp == 1 and player == 1:
            print("Draw")
        elif comp == 2 and player == 2:
            print("Draw")
        elif comp == 3 and player == 3:
            print("Draw")
        elif comp == 1 and player == 3:
            print("Computer Win")
            comp_points += 1
        elif comp == 2 and player == 1:
            print("Computer Win")
            comp_points += 1
        elif comp == 3 and player == 2:
            print("Computer Win")
            comp_points += 1
        elif comp == 3 and player == 1:
            print("You Win")
            player_points += 1
        elif comp == 1 and player == 2:
            print("You Win")
            player_points += 1
        elif comp == 2 and player == 3:
            print("You Win")
            player_points += 1
        else:
            print("Please !!! Enter a Right Option.")
    print("\nYour Score :", player_points)
    print("Computer Score :", comp_points)
    if comp_points < player_points:
        print("""-------------------------
You Won the Game
-------------------------\n""")
    else:
        print("""-------------------------
Computer Won the Game
-------------------------\n""")

if __name__ == "__main__":
    while True:
        print("Do you want to Play the Game ?\n1. Start\n2. Exit")
        val = int(input("Choose an Option : "))
        if val == 1:
            rpsgame()
        elif val == 2:
            quit()
        else:
            print("Error")