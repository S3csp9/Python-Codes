import random
print("It is a Guess Number Game\n")
print("Enter a Number Between 1 to 100\n")
print("No. of Chances - 9 \n")
guess_no = random.randint(0, 100)
no_of_guess = 9
while(no_of_guess > 0):
    print(guess_no)
    no_of_guess = no_of_guess - 1
    entered_number = int(input("Enter a Number - "))
    if guess_no == entered_number:
        print("Congratulations! You guess right.")
        print("No. of guess you took to Finish -", 9-no_of_guess)
        break
    elif guess_no > entered_number:
        print("No. of Chances left -", no_of_guess)
        print("Enter a Greater Number \n")
        continue
    elif guess_no < entered_number:
        print("No. of Chances left -", no_of_guess)
        print("Enter a Lesser Number \n")
        continue
print("_Game Over_")
print("You exceeded your all Chances!!!")