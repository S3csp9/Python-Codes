def getdata():
    import datetime
    return datetime.datetime.now()

def logdata():
    print("For whom you want to Log Data -\n", "1. User_1\n", "2. User_2\n", "3. User_3")
    log = int(input())
    
    if log == 1:
        print("What do you want Log -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_1_Diet.txt", "a") as hd:
                print("Enter what do you want to Add --")
                hdi = input()
                hd.write("Log DateTime - "+str(getdata())+"\nLog Data - "+hdi+"\n\n")
        elif heal == 2:
            with open("User_1_Exercise.txt", "a") as he:
                print("Enter what do you want to Add --")
                hei = input()
                he.write("Log DateTime - "+str(getdata())+"\nLog Data - "+hei+"\n\n")
    
    elif log == 2:
        print("What do you want Log -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_2_Diet.txt", "a") as rd:
                print("Enter what do you want to Add --")
                rdi = input()
                rd.write("Log DateTime - "+str(getdata())+"\nLog Data - "+rdi+"\n\n")
        elif heal == 2:
            with open("User_2_Exercise.txt", "a") as re:
                print("Enter what do you want to Add --")
                rei = input()
                re.write("Log DateTime - "+str(getdata())+"\nLog Data - "+rei+"\n\n")

    elif log == 3:
        print("What do you want Log -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_3_Diet.txt", "a") as ud:
                print("Enter what do you want to Add --")
                udi = input()
                ud.write("Log DateTime - "+str(getdata())+"\nLog Data - "+udi+"\n\n")
        elif heal == 2:
            with open("User_3_Exercise.txt", "a") as ue:
                print("Enter what do you want to Add --")
                uei = input()
                ue.write("Log DateTime - "+str(getdata())+"\nLog Data - "+uei+"\n\n")
    
def retrivedata():
    print("For whom you want to Retrive Data -\n", "1. User_1\n", "2. User_2\n", "3. User_3")
    ret = int(input())
    
    if ret == 1:
        print("What do you want Retrive -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_1_Diet.txt", "rt") as hd:
                print("Your User_1 Diet Chart is Here !!!\n")
                print(hd.read())
        elif heal == 2:
            with open("User_1_Exercise.txt", "rt") as he:
                print("Your User_1 Exercise Chart is Here !!!\n")
                print(he.read())
    
    elif ret == 2:
        print("What do you want Log -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_2_Diet.txt", "rt") as rd:
                print("Your User_2 Diet Chart is Here !!!\n")
                print(rd.read())
        elif heal == 2:
            with open("User_2_Exercise.txt", "rt") as re:
                print("Your User_2 Exrecise Chart is Here !!!\n")
                print(re.read())

    elif ret == 3:
        print("What do you want Log -\n", "1. Diet\n", "2. Exercise")
        heal = int(input())

        if heal == 1:
            with open("User_3_Diet.txt", "rt") as ud:
                print("Your User_3 Diet Chart is Here !!!\n")
                print(ud.read())
        elif heal == 2:
            with open("User_3_Exercise.txt", "rt") as ue:
                print("Your User_3 Exercise Chart is Here !!!\n")
                print(ue.read())

print("! Welcome to our Services !")
print("! This is a Health Management System !")
while(True):
    print(" 1. Start\n", "2. Stop")
    opt = int(input())
    if opt == 1:        
        print("What do you want to do -\n", "1. Log Data\n", "2. Retrive Data\n")
        data = int(input())
        if data == 1:
            try:
                logdata()
            except Exception as Error:
                print(Error)
        elif data == 2:
            try:
                retrivedata()
            except Exception as Error:
                print(Error)
        continue
    elif opt == 2:
        print("Thank You, So much for using our Services")
        break