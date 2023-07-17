from time import time, asctime, sleep
from pygame import mixer

def sound():
    mixer.init()
    mixer.music.load("mixkit.mp3")
    mixer.music.play()
    mixer.music.rewind()
    inp = int(input("Press 1 to stop : "))
    if inp == 1:
        mixer.music.stop()
    else:
        pass

def work_alarm(wait_time):
    print(timing)
    timing = asctime()
    current_time = time()
    while True:
        tim = time() - current_time
        if tim > wait_time:
            print("\nIt's time to take a break.")
            sound()
            print("Now, The 10 minute break time start.")
            sleep(600)
            print("\nIt's time to start the Work Again.")
            sound()
            print("Your 50 minute working timer start.")
            current_time = time()

work_alarm(3000)