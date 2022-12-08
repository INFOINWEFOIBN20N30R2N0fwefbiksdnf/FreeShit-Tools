import colorama,requests,random,threading
from colorama import Fore, init


init()

banner = f"""
{colorama.Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
{colorama.Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
{colorama.Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
{colorama.Fore.GREEN}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
{colorama.Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
{colorama.Fore.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
{colorama.Fore.RED}Created By FreeShit ║ Dev: segations#2344 ║ getfreeshit.today
{colorama.Fore.GREEN}                      Version 1.0.0
"""

print(banner)
user_threads = int(input("Amount of threads: "))

if user_threads > 100:
    print("Use 0 - 100")
    exit(0)

def servergen():
    for x in range(9999):
        ip = str(random.randint(1, 255)) +"." + str(random.randint(1, 255))+"." + str(random.randint(1, 255))+"." + str(random.randint(1, 255))
        requested = requests.get('https://api.mcsrvstat.us/2/{}'.format(ip))

        serveronline = requested.json()["online"]
        port = requested.json()["port"]
        
        
        if requested.json()["ip"] == "127.0.0.1":
            print(f"{ip} connects to 127.0.0.1")
        else:
            print(f"{serveronline} - {ip}:{port}")
    
threads = []
def main(user_threads):
            try:
                for i in range(user_threads):
                    thread = threading.Thread(target=servergen, daemon=True)
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            except:
                pass
def run():
    main(user_threads)
run() 
