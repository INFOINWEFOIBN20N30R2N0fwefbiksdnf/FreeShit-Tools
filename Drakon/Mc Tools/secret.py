import win32api, json, random, win32gui, win32con, threading
from time import sleep

###------------ loading the config ---------------###

keycodes = {
    "a":0x41,
    "b":0x42,
    "c":0x43,
    "d":0x44,
    "e":0x45,
    "f":0x46,
    "g":0x47,
    "h":0x48,
    "i":0x49,
    "j":0x4A,
    "k":0x4B,
    "l":0x4C,
    "m":0x4D,
    "n":0x4E,
    "o":0x4F,
    "p":0x50,
    "q":0x51,
    "r":0x52,
    "s":0x53,
    "t":0x54,
    "u":0x55,
    "v":0x56,
    "w":0x57,
    "x":0x58,
    "y":0x59,
    "z":0x5A,
    "shift":0x10,
    "ctrl":0x11,
    "alt":0x12
}

with open("hyconfig.json") as f:
    cconfig = json.load(f).items()

config = []

for item in cconfig:
    config.append(item)

for item in config:
    try:
        if item[1]["randomized"] is True:
            item[1]["randomized"] = True
        elif item[1]["randomized"] == "true" or "True":
            item[1]["randomized"] = True
        else:
            item[1]["randomized"] = False
    except:
        pass

for item in config:
    try:
        item[1]["keybind"] = keycodes[item[1]["keybind"]]
    except:
        pass

###-------------- setup ----------------###

win_name = config[0][1]

###-------------- cheats :) ---------------###
    
def blockhitting():
    wn = win32gui.FindWindow(None, win_name)
    pos = win32api.MAKELONG(100, 100)
    while True:
        if stop_bh:
            break
        win32api.PostMessage(wn, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
        win32api.PostMessage(wn, win32con.WM_LBUTTONUP, None, pos)
        sleep(config[1][1]["ms between block&hit"] / 1000)
        win32api.PostMessage(wn, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, pos)
        sleep(config[1][1]["block duration ms"] / 1000)
        win32api.PostMessage(wn, win32con.WM_RBUTTONUP, None, pos)
        #randomized hits
        if config[1][1]["randomized"] is True:
            num = random.randint(0, 1)
            if num == 1:
                sleep((config[1][1]["ms between hits"] + config[1][1]["+/- ran"])/ 1000)
            else:
                sleep((config[1][1]["ms between hits"] - config[1][1]["+/- ran"])/1000)
        else:
            sleep(config[1][1]["ms between hits"] / 1000)



def rclick():
    wn = win32gui.FindWindow(None, win_name)
    lParam = win32api.MAKELONG(100, 100)
    while True:
        if stop_rc:
            break
        win32api.PostMessage(wn, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        win32api.PostMessage(wn, win32con.WM_RBUTTONUP, None, lParam)
        #randomized clicks
        if config[2][1]["randomized"] is True:
            num = random.randint(0, 1)
            if num == 1:
                sleep((config[2][1]["ms between clicks"] + config[2][1]["+/- ran"]) / 1000)
            else:
                sleep((config[2][1]["ms between clicks"] - config[2][1]["+/- ran"]) / 1000)
        else:
            sleep(config[2][1]["ms between clicks"] / 1000)


def lclick():
    wn = win32gui.FindWindow(None, win_name)
    pos = win32api.MAKELONG(100, 100)
    while True:
        if stop_lc:
            break
        win32api.PostMessage(wn, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
        win32api.PostMessage(wn, win32con.WM_LBUTTONUP, None, pos)
        #randomized clicks
        if config[3][1]["randomized"] is True:
            num = random.randint(0, 1)
            if num == 1:
                sleep((config[3][1]["ms between clicks"] + config[3][1]["+/- ran"]) / 1000)
            else:
                sleep((config[3][1]["ms between clicks"] - config[3][1]["+/- ran"]) / 1000)
        else:
            sleep(config[3][1]["ms between clicks"] / 1000)

###------------ starting n checking --------------###

stop_bh = True
stop_lc = True
stop_rc = True

while True:
#keybinds n stuff + checks if on/off
    if win32api.GetKeyState(config[1][1]["keybind"]) >=1:
        print("key pressed")
        if stop_bh:
            stop_bh = False
            bhthread = threading.Thread(target = blockhitting)
            bhthread.start()
        else:
            stop_bh = True
            bhthread.join()
    elif win32api.GetKeyState(config[2][1]["keybind"]) >=1:
        print("key pressed")
        if stop_rc:
            stop_rc = False
            rcthread = threading.Thread(target = rclick)
            rcthread.start()
        else:
            stop_rc = True
            rcthread.join()
    elif win32api.GetKeyState(config[3][1]["keybind"]) >=1:
        print("key pressed")
        if stop_lc:
            stop_lc = False
            lcthread = threading.Thread(target = lclick)
            lcthread.start()
        else:
            stop_lc = True
            lcthread.join()
    elif win32api.GetKeyState(config[4][1]["keybind"]) >=1:
        print("exiting")
        exit()
    sleep(0.01)