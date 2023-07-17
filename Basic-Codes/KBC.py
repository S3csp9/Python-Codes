
# This is a KBC Game in which you can answers questions win a certain amount of Money
print("""\n
--------------------------------------
               KBC
      Kaun Banega Crorepati
--------------------------------------""")
questions = ["Which is the National Song ?","Which is National Animal ?","Which is the NAtaional Bird ?"]
# answers = ["Vande Manteram","Tiger","Peacock"]

# This is the Function of the Main game questions
def game():
    Money = 0
    for question in questions:
        print("\n",question)
        if question == questions[0]:
            print("""A. Vande Manteram
B. Jan Gan Mann
C. Ae Vatan
D. Inti Shakti""")
            inpf = input("Choose an Option : ")
            inpvf = inpf.upper()
            if inpvf == "A":
                Money += 100
                # print(Money)
            else:
                print("\nYou Failed because Answer was Wrong !!!")
                break
        elif question == questions[1]:
            print("""A. Lion
B. Bear
C. Tiger
D. Zebra""")
            inps = input("Choose an Option : ")
            inpvs = inps.upper()
            if inpvs == "C":
                Money += 100
                # print(Money)
            else:
                print("\nYou Failed because Answer was Wrong !!!")
                break
        elif question == questions[2]:
            print("""A. Ostrich
B. Peacock
C. Hen
D. Penguin""")
            inpt = input("Choose an Option : ")
            inpvt = inpt.upper()
            if inpvt == "B":
                Money += 100
                # print(Money)
            else:
                print("\nYou Failed because Answer was Wrong !!!")
                break
    print("The Money you won is",Money)

# game()
while True:
    print("""\nDo you want to Play the Game ?
1. Start
2. Exit""")
    inpg = int(input("Choose an Option : "))
    if inpg == 1:
        game()
    elif inpg == 2:
        quit()
    else:
        print("\nChoose a Right Option 1 or 2")