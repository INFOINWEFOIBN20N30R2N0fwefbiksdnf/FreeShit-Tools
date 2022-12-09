from time import sleep
from colorama import Fore,init
import random, string, pyautogui


init()
banner = f"""
{colorama.Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
{colorama.Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
{colorama.Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
{colorama.Fore.GREEN}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
{colorama.Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
{colorama.Fore.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
{colorama.Fore.RED}Created By FreeShit ║ Dev: segations#2344 ║ getfreeshit.today
{colorama.Fore.GREEN}                      Version 2.0.0
"""
print(banner)
chars = string.ascii_letters

churl = input(f"{Fore.RED}enter channel url: ")



def sub(curl):
    pyautogui.click(x=338, y=15)
    pyautogui.click(x=290, y=20)
    pyautogui.click(x=500, y=75)

    pyautogui.write("https://www.youtube.com/create_channel?action_create_new_channel_redirect=true")
    pyautogui.press('enter')
    sleep(2)

    user = []
    for i in range(10):
        user.append(random.choice(string.ascii_letters))
    pyautogui.write(user)
    pyautogui.click(x=571, y=735)
    pyautogui.click(x=976, y=823)
    sleep(5)
    pyautogui.click(x=338, y=15)
    pyautogui.click(x=290, y=20)
    pyautogui.click(x=500, y=75)
    pyautogui.write("curl")
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=1706, y=528)
    sleep(1)

for i in range(10):
    sub()
    sleep(15)
