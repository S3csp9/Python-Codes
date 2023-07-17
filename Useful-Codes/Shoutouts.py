from win32com.client import Dispatch

def speaks(str):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(str)

def add_name():
    name = input("\nEnter the Name : ")
    names.append(name)

names = []
if __name__ == '__main__':
    while True:
        inp = int(input("\nDo you want to start the Program? \n1. Start \n2. Exit \nEnter a Input : "))
        if inp == 1:
            add_name()
            while True:
                new = int(input("Do you want to add more names? \n1. Yes \n2. No \nOption : "))
                if new == 1:
                    add_name()
                elif new == 2:
                    break
                else:
                    print("Enter a Valid Input.")
            print("\n")
            for naam in names:
                print(f"Shoutout to {naam}")
                speaks(f"Shoutout to {naam}")
        elif inp == 2:
            quit()
        else:
            print("You Entered a Wrong Input.")