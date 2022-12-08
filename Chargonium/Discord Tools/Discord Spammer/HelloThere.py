list = open("Text.list", "r").readlines()
banner = """
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
Created By FreeShit ║ Dev: Chargonium#8203 ║ getfreeshit.today
                      Version 1
"""
banner = """
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
Created By FreeShit ║ Dev: Chargonium#8203 ║ getfreeshit.today
                      Version 1
"""
print(banner)

import pyautogui

from time import sleep
from random import randrange
for i in range(10_000):
    Word = list[randrange(0, len(list) - 1)]
    Word = Word.removesuffix("\n")
    print(Word)
    pyautogui.moveTo(550, 980)
    sleep(0.5)
    pyautogui.click()
    sleep(0.5)
    pyautogui.write(Word, interval=0.01)
    pyautogui.press('enter')
    sleep(10)