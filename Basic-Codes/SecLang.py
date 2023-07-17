import string
import random
# This is a Secret Language Program
print("""
---------------------------------
        Welcoe to our
    Secret Language Program
---------------------------------""")

def encode():
    message = input("\nEnter the Message : ")
    if len(message) <= 3:
        print("The Coded Message is :",encoded[::-1])
    else:
        r1 = ''.join(random.choice(string.ascii_lowercase) for x in range(3))
        r2 = ''.join(random.choice(string.ascii_lowercase) for x in range(3))
        encoded = r1+message[1:]+message[0]+r2
        print("The Coded Message is :",encoded)

def decode():
    code = input("\nEnter the Message : ")
    if len(code) <= 3:
        print("The Message is :",code[::-1])
    else:
        decoded = code[-4]+code[3:-4]
        print(decoded)

if __name__ == "__main__": 
    while True:
        print("\nWhat do you want:\n1. Start\n2. Exit")
        inp = int(input("Choose an Option : "))
        if inp == 1:
            print("\nWhat do you want:\n1. Encode\n2. Decode")
            val = int(input("Choose an Option : "))
            if val == 1:
                encode()
            elif val == 2:
                decode()
            else:
                print("You Entered Wrong Option.")
        elif inp == 2:
            print("Thank you for using our Program !!!")
            quit()
        else:
            print("Choose a Right Option.")