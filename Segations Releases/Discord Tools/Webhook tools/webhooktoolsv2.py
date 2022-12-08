import os,requests,string,random,json, colorama,threading
from time import sleep
from colorama import Fore,init
from rich.console import Console
from rich.markdown import Markdown

init()

os.system("title WebHook Tools Created by getfreeshit.today")

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

useragents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8064573025028230361 t2351350612522939859 ath259cea6f altpriv cvcv=2 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6468977051454352589 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v4048279444232390072 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v2672887183238113917 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0"
] 


def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


with open("webhooks.txt") as f:
    words = f.read().splitlines()


def threadmultispammer():
    
    print("""
(E) @Everyone Spam
(M) Message Basic Spam
          """)
    modes = input("What Mode >> ")

    if modes == "E" or modes == "e":
        message = input("What's the message after the ping >> ")
    if modes == "M" or modes == "m":
        title = input("Title: ")
        description = input("Description: ")
        print("ADD http:// or https// or leave blank to use ours")
        image = input("Image Url: ")
    user_threads = input("How Many Threads: ")
    amount = input("Amount of messages: ")
    
    if modes == "E" or modes == "e":
        i = 0
        for x in range(int(amount)):
            url = random.choice(words)
            payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "content": "@everyone {}".format(message)
    })
            headers = {
        'Content-Type': 'application/json'
        }

            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    
    if modes == "M" or modes == "m":
        payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "embeds": [
        {
        "title": title,
        "description": description,
        "color": "124",
        "fields": [
            {
            "name": "hi",
            "value": "insane"
            }
        ],
        "footer": {
            "text": "Devious Apple",
            "icon_url": "https://i.imgur.com/tN5qXJy.jpeg"
        },
        "image": {
            "url": image
        }
        }
    ]
    })

        headers = {
        'Content-Type': 'application/json'
        }
        i = 0
    
    
        for x in range(int(amount)):
            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
        threads = []
    def main(user_threads):
            try:
                for i in range(user_threads):
                    thread = threading.Thread(target=threadmultispammer, daemon=True)
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            except KeyboardInterrupt:
                exit(0)
            except:
                pass

    def run():
            main(user_threads)

    run()

def multispammer():
    
    print("""
(E) @Everyone Spam
(M) Message Basic Spam
          """)
    modes = input("What Mode >> ")

    if modes == "E" or modes == "e":
        message = input("What's the message after the ping >> ")
    if modes == "M" or modes == "m":
        title = input("Title: ")
        description = input("Description: ")
        print("ADD http:// or https// or leave blank to use ours")
        image = input("Image Url: ")
    amount = input("Amount of messages: ")


    
    
    if modes == "E" or modes == "e":
        i = 0
        for x in range(int(amount)):
            url = random.choice(words)
            payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "content": "@everyone {}".format(message)
    })
            headers = {
        'Content-Type': 'application/json'
        }

            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    
    if modes == "M" or modes == "m":
        i = 0
        for x in range(int(amount)):
            url = random.choice(words)
            payload = json.dumps({
        "username": get_random_string(10),
        "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
        "embeds": [
            {
            "title": title,
            "description": description,
            "color": "124",
            "fields": [
                {
                "name": "hi",
                "value": "insane"
                }
            ],
            "footer": {
                "text": "Devious Apple",
                "icon_url": "https://i.imgur.com/tN5qXJy.jpeg"
            },
            "image": {
                "url": image
            }
            }
        ]
        })

            headers = {
            'Content-Type': 'application/json'
            }
        
        
            
            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
        

def threadspammer():
    
    print("""
(E) @Everyone Spam
(M) Message Basic Spam
          """)
    modes = input("What Mode >> ")
    
    webhook = input("Target webhook: ")
    if modes == "E" or modes == "e":
        message = input("What's the message after the ping >> ")
    if modes == "M" or modes == "m":
        title = input("Title: ")
        description = input("Description: ")
        print("ADD http:// or https// or leave blank to use ours")
        image = input("Image Url: ")
    user_threads = input("How Many Threads: ")
    amount = input("Amount of messages: ")


    url = webhook
    
    if modes == "E" or modes == "e":
        i = 0
        for x in range(int(amount)):
        
            payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "content": "@everyone {}".format(message)
    })
            headers = {
        'Content-Type': 'application/json'
        }

            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    
    if modes == "M" or modes == "m":
        payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "embeds": [
        {
        "title": title,
        "description": description,
        "color": "124",
        "fields": [
            {
            "name": "hi",
            "value": "insane"
            }
        ],
        "footer": {
            "text": "Devious Apple",
            "icon_url": "https://i.imgur.com/tN5qXJy.jpeg"
        },
        "image": {
            "url": image
        }
        }
    ]
    })

        headers = {
        'Content-Type': 'application/json'
        }
        i = 0
    
    
        for x in range(int(amount)):
            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    threads = []
    def main(user_threads):
            try:
                for i in range(user_threads):
                    thread = threading.Thread(target=threadspammer, daemon=True)
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            except KeyboardInterrupt:
                exit(0)
            except:
                pass

    def run():
            main(user_threads)

    run()

def spammer():
    
    print("""
(E) @Everyone Spam
(M) Message Basic Spam
          """)
    modes = input("What Mode >> ")
    
    webhook = input("Target webhook: ")
    if modes == "E" or modes == "e":
        message = input("What's the message after the ping >> ")
    if modes == "M" or modes == "m":
        title = input("Title: ")
        description = input("Description: ")
        print("ADD http:// or https// or leave blank to use ours")
        image = input("Image Url: ")
    amount = input("Amount of messages: ")


    url = webhook
    
    if modes == "E" or modes == "e":
        i = 0
        for x in range(int(amount)):
        
            payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "content": "@everyone {}".format(message)
    })
            headers = {
        'Content-Type': 'application/json'
        }

            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    
    if modes == "M" or modes == "m":
        payload = json.dumps({
    "username": get_random_string(10),
    "avatar_url": "https://i.imgur.com/tN5qXJy.jpeg",
    "embeds": [
        {
        "title": title,
        "description": description,
        "color": "124",
        "fields": [
            {
            "name": "hi",
            "value": "insane"
            }
        ],
        "footer": {
            "text": "Devious Apple",
            "icon_url": "https://i.imgur.com/tN5qXJy.jpeg"
        },
        "image": {
            "url": image
        }
        }
    ]
    })

        headers = {
        'Content-Type': 'application/json'
        }
        i = 0
    
    
        for x in range(int(amount)):
            i+=1
            print(f"Sent {str(i)} message to webhook")
            requests.post(url, headers=headers, data=payload)
    
               

def gen():
    print(banner)
    amount = input("Amount >> ")
    i = 0
    for x in range(int(amount)):
        i += 1
        N = 68
        res = ''.join(random.choices(string.ascii_letters +
                                    string.digits, k=N))
        semen = random.randint(1000000000000000000, 9999999999999999999)
        print("https://discord.com/api/webhooks/" + str(semen) + "/" + str(res) + " - " + str(i))
    
def checker():
    print(banner)
    webhook = input("Webhook >> ")
    r = requests.get(webhook, headers={'User-Agent': random.choice(useragents)})
    status = r.status_code
    
    if status == 200:
        print(webhook + " - Is Valid: 200")
        data = r.json()
        types = data["type"]
        ids = data["id"]
        name = data["name"]
        avatar = data["avatar"]
        channelid = data["channel_id"]
        guildid = data["guild_id"]
        appid = data["application_id"]
        token = data["token"]
        print(f"""
INFO:

Type - {types}
id - {ids}
name - {name}
avatar - {avatar}
channel id - {channelid}
guild id - {guildid}
application id - {appid}
token - {token}""")
    elif status == 404:
        print(webhook + " - Is Invalid: 404")
    
def genandchecker():
    print(banner)
    amount = input("Amount >> ")
    i = 0
    for x in range(int(amount)):
        i +=1
        N = 68
        res = ''.join(random.choices(string.ascii_letters +
                                string.digits, k=N))
        semen = random.randint(1000000000000000000, 9999999999999999999)
        webhook = "https://discord.com/api/webhooks/" + str(semen) + "/" + str(res)
        
        r = requests.get(webhook, headers={'User-Agent': random.choice(useragents)})
        
        if r.status_code == 200:
            print(webhook + " - is valid: 200 - " + str(i))
        if r.status_code == 404:
            print(webhook + " - is invalid: 404 - " + str(i))
    
def deleter():
    webhook = input("Webhook >> ")
    requests.delete(webhook)
    CheckingWebStatus = requests.get(webhook)
    if CheckingWebStatus.status_code == 404:
        print(f"Webhook has been deleted Or is invalid")
    elif CheckingWebStatus.status_code == 200:
        print(f"Failed to delete Webhook")
    
def mainmenu():
    print(banner)
    markdown_mainmenu = """
# Select the feature you want to use.
[S] Spammer Shit
[I] Info Shit
[M] Misc Shit"""

    console = Console()
    md = Markdown(markdown_mainmenu)
    console.print(md) 
    features = input(">> ")
    print(colorama.Fore.GREEN)
    
    if features == "S" or features == "s":
        print("""[S] Spammer
[MS] Multi Spammer
[TS] Thread Spammer
[MTS] Multi Thread Spammer""")
        options = input(">> ")
        if options == "S" or options == "s":
            spammer()
            sleep(2)
            mainmenu()
        elif options == "ms" or options == "MS":
            multispammer()
            sleep(2)
            mainmenu()
        elif options == "TS" or options == "ts":
            threadspammer()
            sleep(2)
            mainmenu()
        elif options == "mts" or options == "MTS":
            threadmultispammer()
            sleep(2)
            mainmenu()
    elif features == "i" or features == "I":
        print("""[C] Checker + info
[GC] Gen and check and info""")
        options = input(">> ")
        if options == "C" or options == "c":
            checker()
            sleep(2)
            mainmenu()
        elif options == "GC" or options == "gc":
            genandchecker()
            sleep(2)
            mainmenu()
    elif features == "M" or features == "m":
        print("""[G] Gen
[D] Webhook Deleter""")
        options = input(">> ")
        if options == "G" or options == "g":
            gen()
            sleep(2)
            mainmenu()
        elif options == "D" or options == "d":
            deleter()
            sleep(2)
            mainmenu()
    
    
mainmenu()