import os
try:
    import random
    import time
    from colorama import Fore
    from javascript import require, On, Once, AsyncTask, once, off
except:
    os.system('pip install colorama javascript')
    import random
    import time
    from colorama import Fore
    from javascript import require, On, Once, AsyncTask, once, off
def banner():
    print(f"{Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗ ")
    time.sleep(0.2)
    print(f"{Fore.BLUE}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝ ")   
    time.sleep(0.2)
    print(f"{Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║    ")   
    time.sleep(0.2)
    print(f"{Fore.BLUE}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    ") 
    time.sleep(0.2)  
    print(f"{Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║    ")   
    time.sleep(0.2)
    print(f"{Fore.BLUE}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    ") 
    time.sleep(0.2)  
    print(f"{Fore.RED}Created By FreeShit ║ getfreeshit.today") 
    print(f"{Fore.WHITE}")

FreeShitMineFlayer = require('mineflayer')
banner()


def microsoft(ip: str, port: str, username: str, password: str):
    bot = FreeShitMineFlayer.createBot({'auth': 'microsoft', 'host': ip, 'port': port, 'username': username, 'password': password, 'hideErrors': False })
    print("[Successful] Sent Account to that server " + str(ip)  + ":" + str(port))

def cracked(server: str, port: str,name: str, amount: str):
    for x in range(int(amount)):
        cock = name + "_" + str(random.randint(1, 9999))
        bot = FreeShitMineFlayer.createBot({'auth': 'cracked', 'host': str(server), 'port': str(port), 'username': cock})
        print(cock + " Has Joined")
    print(f"Server IP: {server}")
    print(f"Server Port: {port}")
    print(f"Bot Usernames: {name}")
    print(f"Bot Amount Sent: {amount}")
    print("Status: Bots Have Been Sent Successfully")
    
wee = input('cracked (c) or microsoft (m): ')
if wee == 'c':
    a = input('ip (default is 25565): ')
    b = input('port: ')
    c = input('name: ')
    d = input('amount: ')
    cracked(a,b,c,d)
elif wee == 'm':
    a = input('ip (25565)')
    b = input('port: ')
    c = input('username: ')
    d = input('password: ')
    microsoft(a,b,c,d)