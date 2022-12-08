import os, random,sys,time, win32gui, win32api, win32con,keyboard,colorama,json
from time import sleep
from colorama import Fore

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)
        
with open("config.json") as file:
    jsonInfo = json.load(file)
    mcname = jsonInfo["MC_WINDOW_NAME"]
    stopkey = jsonInfo["STOP_KEY"]
    
    maxrightdelay = jsonInfo["RIGHT_MAX_DELAY"]
    minrightdelay = jsonInfo["RIGHT_MIN_DELAY"]
        
    maxleftdelay = jsonInfo["LEFT_MAX_DELAY"]
    minleftdelay = jsonInfo["LEFT_MIN_DELAY"]

def subtract(x,y):
    return x - y

def times(x,y):
    return x * y

def divide(x,y):
    return x / y

def add(x,y):
    return x + y

def secretmenu():
    os.system("title CalClicker made by freeshit ║ getfreeshit.today") 
    #os.system("cls")
    print(f"""
{colorama.Fore.LIGHTBLUE_EX}  
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║   
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║   
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
 ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝
██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Made:
Made by segation / Freeshit / getfreeshit.today / Build - 1042713

Clicker:
[LC] Left Clicker ║ [RC] Right Clicker ║ [B] Both Clickers

Misc:
[I] Info ║ [M] Main menu ║ [C] Clear Console
              """)
    feature2 = input(">> ")     
    if feature2 == "LC" or feature2 == "lc":
            hprint("Starting Left Clicker")
            sleep(1)
            hprint("Successfully Started")
            leftclicker()
    elif feature2 == "C" or feature2 == "c":
            os.system("cls")
            secretmenu()
    elif feature2 == "RC" or feature2 == "rc":
            hprint("Starting Right Clicker")
            sleep(1)
            hprint("Successfully Started")
            rightclicker()
    elif feature2 == "B" or feature2 == "b":
            hprint("Starting Both the Clickers")
            sleep(1)
            hprint("Successfully Started")
            bothclicker()       
    elif feature2 == "I" or feature2 == "i":
            print(f"""
Stop Key: {stopkey}
Right Delay: 
{maxrightdelay}
{minrightdelay}
Left Delay:
{maxleftdelay}
{minleftdelay}
Window Title: {mcname}""")
            time.sleep(3)
            secretmenu()
    elif feature2 == "M" or feature2 == "m":
            os.system("cls")
            menu()
    else:
        os.system("cls")
        secretmenu()

def menu():
    os.system("title Python Calculator") 
    print(f"""{colorama.Fore.GREEN}
          
                     ▄▄                      ▄▄                                 
  ▄▄█▀▀▀█▄█        ▀███                    ▀███           ██                    
▄██▀     ▀█          ██                      ██           ██                    
██▀       ▀▄█▀██▄    ██  ▄██▀██▀███  ▀███    ██  ▄█▀██▄ ██████  ▄██▀██▄▀███▄███ 
██        ██   ██    ██ ██▀  ██  ██    ██    ██ ██   ██   ██   ██▀   ▀██ ██▀ ▀▀ 
██▄        ▄█████    ██ ██       ██    ██    ██  ▄█████   ██   ██     ██ ██     
▀██▄     ▄▀█   ██    ██ ██▄    ▄ ██    ██    ██ ██   ██   ██   ██▄   ▄██ ██     
  ▀▀█████▀▀████▀██▄▄████▄█████▀  ▀████▀███▄▄████▄████▀██▄ ▀████ ▀█████▀▄████▄                                           
""")
    print("Select a feature")
    print("""
[+] Add ║ [-] Subract ║ [/] Divide ║ [X] Times ║ [AC] clear console
""")
    feature = input(">> ")
    
    if feature == "+":
        print("You selected Plus")
        number1 = float(input("First Number >> "))
        number2 = float(input("Second Number >> "))
        print(number1, "+", number2, "=", add(number1, number2))
        #time.sleep(3)
        menu()
    elif feature == "AC" or feature == "ac":
        os.system("cls")
        menu()
    elif feature == "-":
        print("You selected Minus")
        number1 = float(input("First Number >> "))
        number2 = float(input("Second Number >> "))
        print(number1, "-", number2, "=", subtract(number1, number2))
        #time.sleep(3)
        menu()
    elif feature == "/":
        print("You selected Divide")
        number1 = float(input("First Number >> "))
        number2 = float(input("Second Number >> "))
        print(number1, "/", number2, "=", divide(number1, number2))
        #time.sleep(3)
        menu()
    elif feature == "X" or feature == "x":
        print("You selected Times")
        number1 = float(input("First Number >> "))
        number2 = float(input("Second Number >> "))
        print(number1, "*", number2, "=", times(number1, number2))
        #time.sleep(3)
        menu()
        
 

# SECRET MENU SHIT AND ALL IDK FUCK LIFE IG       
        
    elif feature == "SM" or feature == "sm":
        os.system("cls")
        secretmenu()
    else: 
        print("Thats not a feature")
        menu()
    
    
def bothclicker():       
    while True:
        hWnd = win32gui.FindWindow(None, mcname)
        lParam = win32api.MAKELONG(100, 100)
        if keyboard.is_pressed(stopkey):
                secretmenu()
        if win32api.GetKeyState(0x01)<0:
            lcsleep = random.uniform(minleftdelay, maxleftdelay)
            sleep(lcsleep)
            win32api.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)  
        if win32api.GetKeyState(0x02)<0:
            rcsleep = random.uniform(minrightdelay, maxrightdelay)
            sleep(rcsleep)
            win32api.PostMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
            win32api.PostMessage(hWnd, win32con.WM_RBUTTONUP, None, lParam)
    
def rightclicker():
    while True:
        hWnd = win32gui.FindWindow(None, mcname)
        lParam = win32api.MAKELONG(100, 100)
        if keyboard.is_pressed(stopkey):
                secretmenu()
        if win32api.GetKeyState(0x02)<0:
            rcsleep = random.uniform(minrightdelay, maxrightdelay)
            sleep(rcsleep)
            win32api.PostMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
            win32api.PostMessage(hWnd, win32con.WM_RBUTTONUP, None, lParam)

def leftclicker():
    while True:
        hWnd = win32gui.FindWindow(None, mcname)
        lParam = win32api.MAKELONG(100, 100)
        if keyboard.is_pressed(stopkey):
                secretmenu()
        if win32api.GetKeyState(0x01)<0:    
            lcsleep = random.uniform(minleftdelay, maxleftdelay)
            sleep(lcsleep)
            win32api.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)  
                       
menu()