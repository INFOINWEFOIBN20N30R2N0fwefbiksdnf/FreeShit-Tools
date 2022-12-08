import os,requests,sys,time
from colorama import Fore, init

init()
color = Fore

banner = """
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
Created By FreeShit ║ Dev: segations#2344 ║ getfreeshit.today
"""

os.system("title Kahoot Botter Created by getfreeshit.today")

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

    
print(color.GREEN)
print(banner)
hprint("Starting Kahoot Botter...")
print(color.BLUE)
hprint("Created By FreeShit ║ getfreeshit.today...")
print(color.RED)
hprint("Developer: segations#2344")
print(color.GREEN)
gamepin = input("GamePin >> ")
botname = input("Bot Name >> ")
botamount = input("Bot Amount >> ")
    
hprint(f"Sending {str(botamount)} bots...")    
r = requests.post("https://kahootbotter.com/api/graphql", json={"operationName":"spawnBots","variables":{"botName":str(botname),"gamePin":int(gamepin),"botAmount":int(botamount),"sessionId":"0.0.0.1"},"query":"mutation spawnBots($botName: String!, $gamePin: Int!, $botAmount: Int!, $sessionId: String!) {\n  spawnBots(\n    botName: $botName\n    gamePin: $gamePin\n    botAmount: $botAmount\n    sessionId: $sessionId\n  ) {\n    title\n    status\n    description\n    __typename\n  }\n}\n"}, headers={'Content-type': 'application/json'})
if r.status_code == 200:
    print("Sent Successfully Status code 200")
elif r.status_code == 404:
    print("Error status code 404")
