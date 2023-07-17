from pygame import mixer
from time import time, asctime

timing = asctime()

def waterlog():
    with open("Water_log.txt", "a") as waterfile:
        waterfile.write("You have Drank water at "+timing+"\n")

def eyeslog():
    with open("Eyes_log.txt", "a") as eyesfile:
        eyesfile.write("You have Done Eyes Exercise at "+timing+"\n")
def physicallog():
    with open("Physical_log.txt", "a") as physicalfile:
        physicalfile.write("You have Done Physical Exercise at "+timing+"\n")

def wateralarm():
    while(True):
        mixer.init()
        mixer.music.load("song.mp3")
        mixer.music.set_volume(50)
        mixer.music.play()
        print("Have you Drink Water?", 
        "If yes, type 'Done' - ")
        inpwater = input().upper()
        if inpwater == "DONE":
            mixer.music.stop()
            waterlog()
            print("OK! Work logged in File")
            break

def eyesalarm():
    while(True):
        mixer.init()
        mixer.music.load("song.mp3")
        mixer.music.set_volume(50)
        mixer.music.play()
        print("Have you Done Eyes Exercise?", 
        "If yes, type 'Done' - ")
        inpeye = input().upper()
        if inpeye == "DONE":
            mixer.music.stop()
            eyeslog()
            print("OK! Work logged in File")
            break

def physicalalarm():
    while(True):
        mixer.init()
        mixer.music.load("song.mp3")
        mixer.music.set_volume(50)
        mixer.music.play()
        print("Have you Done Physical Exerise?", 
        "If yes, type 'Done' - ")
        inphysical = input().upper()
        if inphysical == "DONE":
            mixer.music.stop()
            physicallog()
            print("OK! Work logged in File")
            break

if __name__ == '__main__':
    water_time = time()
    eyes_time = time()
    physical_time = time()
    water_secs = 3600
    eyes_secs = 1800
    physical_secs = 7200
    print("This is a Always be Healthy Program,\nWhich Always Keeps you Healthy --")
    while (True):
        if time() - water_time > water_secs:
            wateralarm()
            water_time = time()
        if time() - eyes_time > eyes_secs:
            eyesalarm()
            eyes_time = time()
        if time() - physical_time > physical_secs:
            physicalalarm()
            physical_time = time()



