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
id = input(Colorate.Vertical(Colors.purple_to_blue, "ID >",1))
r = requests.get(f"https://api.discord.name/api/user/{id}")
data = r.json()
success = data["success"]
maindata = data["data"]
ids = maindata["id"]
username = maindata["username"]
avatar = maindata["avatar"]
banner = maindata["banner"]
bannercolor = maindata["bannerColor"]
created = maindata["created"]
if r.status_code == 200:
    print(Colorate.Vertical(Colors.purple_to_blue,f"""
Success - {success}
ID - {ids}
Username - {username}
Avatar - {avatar}
Banner - {banner}
Banner Color - {bannercolor}
Created - {created}""",1))
if r.status_code == 400:
    print(Colorate.Vertical(Colors.purple_to_blue,f"{id} is invalid", 1))