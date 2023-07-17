# This is a Calculator Program which is used to solve two values.
print("This is a Two Value Calci.\n")
# Here, we Start the Program
while True:
    try:
        num1 = int(input("Enter the First Value : "))
        num2 = int(input("Enter the Second Value : "))
        print("""What Operation do you want to perform
            1. Division (/)
            2. Float Division (//)
            3. Multiplication (*)
            4. Addition (+)
            5. Substraction (-)
            6. Power (**)
            7. Remainder (%)
            """)
        oper = int(input("Choose an Option from Above Operations : "))

        # Now, We will write the Operation funtions
        if oper == 1:
            print(num1,"/",num2,"=",num1/num2)
        elif oper == 2:
            print(num1,"//",num2,"=",num1//num2)
        elif oper == 3:
            print(num1,"*",num2,"=",num1*num2)
        elif oper == 4:
            print(num1,"+",num2,"=",num1+num2)
        elif oper == 5:
            print(num1,"-",num2,"=",num1-num2)
        elif oper == 6:
            print(num1,"**",num2,"=",num1**num2)
        elif oper == 7:
            print(num1,"%",num2,"=",num1%num2)
        else:
            print("Please! Choose a Right Option between 1 to 7.\n")
    except ValueError:
        print("Error. Please provide Correct Value or Option.\n")