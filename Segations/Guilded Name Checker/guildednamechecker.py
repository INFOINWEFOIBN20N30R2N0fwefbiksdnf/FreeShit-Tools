import requests
from pystyle import Colorate, Colors
print(Colorate.Vertical(Colors.purple_to_blue, """
                ███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
                ██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
                █████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
                ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
                ██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
                ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
                Created By FreeShit ║ getfreeshit.today


""",1))

name = input(Colorate.Vertical(Colors.purple_to_blue, "Name >",1))
r = requests.get(f'https://www.guilded.gg/api/subdomains/u/{name}')
if not r.text == "{}":
    print(Colorate.Vertical(Colors.purple_to_blue, f"{name} is taken",1))
elif r.text == "{}":
    print(Colorate.Vertical(Colors.purple_to_blue, f"{name} is not taken",1))
