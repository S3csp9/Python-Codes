import time
form = time.strftime("%I:%M:%S %p")
print(form)
hour = int(time.strftime("%I"))
sett = time.strftime("%p")
if hour>=6 and sett=="AM":
    print("Good Morning !!!")
elif hour>=0 and sett=="PM":
    print("Good Afternoon !!!")
elif hour>=6 and sett=="PM":
    print("Good Evening !!!")
elif hour>=10 and sett=="PM":
    print("Good Night !!!")
elif hour>=0 and sett=="PM":
    print("Good Night !!!")