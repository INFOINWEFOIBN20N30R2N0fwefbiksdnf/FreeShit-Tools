import os,glob,psutil
from pystyle import Colorate, Colors
from colorama import Fore
from re import findall
from time import sleep

username = os.getenv('username')
os.system('title FreeShit ║ Roblox Server IP Grabber')

def CheckForRunningProccess(processName):
    for procceeses in psutil.process_iter():
        try:
            if processName.lower() in procceeses.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if CheckForRunningProccess('RobloxPlayerBeta'):
    sleep(1)
    os.system('title FreeShit ║ Finding Roblox Process')
    print("Finding Roblox Process")
    sleep(2)
    os.system('title FreeShit ║ Found Process')
    print(Colorate.Vertical(Colors.green_to_blue, """
    ███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
    █████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
    ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
    ██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
    
    Created By FreeShit ║ getfreeshit.today
    [!] [Success] - Roblox Process has been found""",1))
    try:
        input(Colorate.Vertical(Colors.green_to_blue,"    [!] When Game Fully loads press [Enter] to get ip", 1))
    except SyntaxError:
        pass
    os.system('title FreeShit ║ Sectioning out IP')
    sleep(1)
    appdatarobloxlogs = glob.glob(r'C:\users\{}\AppData\Local\Roblox\logs\*'.format(username))
    latestlog = max(appdatarobloxlogs, key=os.path.getctime)
    robloxlogs = open(latestlog, 'r')
    for bobux in robloxlogs:
        if 'Connection accepted from' in bobux:
            bobux1 = bobux.replace('Connection accepted from', '')
            bobux2 = bobux1.replace('|', ':')
            bobuxip = findall(r'\d+(?:\.\d+){3}:\d+', bobux2)
            bobuxip[-1] = f"{bobuxip[-1]}"
            os.system(f'title FreeShit ║ IP = {str(bobuxip)}')
            print(Colorate.Vertical(Colors.green_to_blue,f"    [!] Server IP: {str(bobuxip)}",1) + Fore.WHITE)    

else:
    print(f"""
          {Fore.RED}
          ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
            Roblox is not running
             Please Start Roblox 
          ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
          {Fore.WHITE}""")