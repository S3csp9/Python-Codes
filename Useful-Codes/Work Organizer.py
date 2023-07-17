import os
# This program removes the extra data from the folder and reorder all the files as in the number order and some exxception are also being accepted

def cluster():
    os.chdir(path)
    make_list = os.listdir()
    i = 1
    for file in make_list:
        if file.endswith(formatt):
            typee = f"{i}{formatt}"
            os.rename(file, typee)
            i += 1
        else:
            pass

while True:
    print("This is a Cluster Remover Program")
    print("What do you want ?\n1. Start\n2. Exit")
    inp =  int(input("Choose an Option : "))
    if inp == 1:
        path = input("Enter the Full Path of the File : ")
        typ = input("Enter the Format you want to Organize : ")
        formatt = ("."+typ.lower())
        cluster()
    elif inp == 2:
        quit()
    else:
        print("Please !!! Enter Right Option.")