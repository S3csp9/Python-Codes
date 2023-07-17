print('This is a Astrologers Star Game')
n = int(input("Enter No. of Rows you want : "))
Dir = int(input("Upward(0) and Downward(1) : "))
bol = bool(Dir)

if bol == True:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*",end="")
        print()

elif bol == False:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()