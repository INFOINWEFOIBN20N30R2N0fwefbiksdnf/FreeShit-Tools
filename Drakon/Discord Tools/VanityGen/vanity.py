import os
try:
    import asyncio
    import aiohttp as aiohttp
    import time
    from bs4 import BeautifulSoup
    import requests
    import threading
    from random_word import RandomWords
    from colour import Color
    from colorama import Fore
    from pystyle import Colorate, Colors, Center
except:
    os.system('pip install aiohttp asyncio bs4 pystyle Random-Word==1.0.10 requests')
    import asyncio
    import aiohttp as aiohttp
    import time
    from bs4 import BeautifulSoup
    import requests
    import threading
    from random_word import RandomWords
    from colour import Color
    from colorama import Fore
    from pystyle import Colorate, Colors, Center
    
word = RandomWords()
working = []
checked = []
proxy_list = []
vanit = []

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.purple_to_blue, """


                                              ▄▄         ▄▄                                   
▀███▀▀▀███                            ▄█▀▀▀█▄███         ██   ██      ▀████▀                  
  ██    ▀█                           ▄██    ▀███              ██        ██                    
  ██   █ ▀███▄███  ▄▄█▀██  ▄▄█▀██    ▀███▄    ███████▄ ▀███ ██████      ██ ▀████████▄  ▄██▀██ 
  ██▀▀██   ██▀ ▀▀ ▄█▀   ██▄█▀   ██     ▀█████▄██    ██   ██   ██        ██   ██    ██ ██▀  ██ 
  ██   █   ██     ██▀▀▀▀▀▀██▀▀▀▀▀▀   ▄     ▀████    ██   ██   ██        ██   ██    ██ ██      
  ██       ██     ██▄    ▄██▄    ▄   ██     ████    ██   ██   ██        ██   ██    ██ ██▄    ▄
▄████▄   ▄████▄    ▀█████▀ ▀█████▀   █▀█████▀████  ████▄████▄ ▀████   ▄████▄████  ████▄█████▀ 
                                                                                              

  _       __    _      _  _____  _         __    ____  _    
 \ \  /  / /\  | |\ | | |  | |  \ \_/     / /`_ | |_  | |\ |
  \_\/  /_/--\ |_| \| |_|  |_|   |_|      \_\_/ |_|__ |_| \|


Created By FreeShit ║ getfreeshit.today 


""",1))


### ---------------- proxy scraper ---------------- ###

def proxy_scrape():
    global proxy_list
    proxy_list = []
    funni_list = requests.get('https://www.proxy-list.download/api/v1/get?type=http').text
    lines = funni_list.splitlines()
    for i in range(len(lines)):
        if lines[i] in proxy_list:
            pass
        else:
            proxy_list.append([i])
            
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    lines = text.splitlines()  
    for i in range(299):
        if lines[i+3] in proxy_list:
            pass
        else:
            proxy_list.append(lines[i+3])
    html = requests.get('https://us-proxy.org/').text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    lines = text.splitlines()  
    for i in range(199):
        if lines[i+3] in proxy_list:
            pass
        else:
            proxy_list.append(lines[i+3])
            
            
### ----------- vanity checker ------------- ###
    
async def checke(url, proxy, vanity):
    global vanit
    timeout = 10
    try:
        session_timeout = aiohttp.ClientTimeout(
            total = None,
            sock_connect = timeout,
            sock_read = timeout,
        )
        async with aiohttp.ClientSession(timeout = session_timeout) as session:
            async with session.get(url, proxy = f'http://{proxy}', timeout = timeout) as resp:
                pass
    except Exception as error:
        pass
    else:
        if resp.status == 404:
            vanit.append(vanity)
        
async def vanitygen(sad1,sad2):
    global working
    tasks = []
    api = "https://discord.com/api/v8/invites/"
    for i in range(len(working)):
        while True:
            ran = word.get_random_word(minLength = sad1,maxLength = sad2)
            if ran is not None:
                break
        url = api + ran
        task = asyncio.create_task(checke(url, working[i],f"\n/{ran}"))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
### ----------- proxy checker ------------- ###
    
async def checker(url, proxy):
    global checked
    timeout = 10
    try:
        session_timeout = aiohttp.ClientTimeout(
            total = None,
            sock_connect = timeout,
            sock_read = timeout,
        )
        async with aiohttp.ClientSession(timeout = session_timeout) as session:
            async with session.get(url, proxy = f'http://{proxy}', timeout = timeout) as resp:
                pass
    except Exception as error:
        pass
    else:
        checked.append(proxy)

        
        
async def main():
    proxy_scrape()
    global working, proxy_list, checked
    tasks = []
    count = 0
    for i in range(len(proxy_list)):
        task = asyncio.create_task(checker('https://api.ipify.org/', proxy_list[i]))
        tasks.append(task)
    await asyncio.gather(*tasks)
    for i in range(len(checked)):
        if checked[i] in working:
            pass
        else:
            working.append(checked[i])
    
### ----------- threading n shit ----------- ###

def vanity(wee1,wee2,reps):
    global how, wurl, filen, sow, filep
    for i in range(reps):
        asyncio.run(vanitygen(wee1,wee2))
        time.sleep(30)
    if how == 'w':    
        if len(vanit) <= 20:
            payload = {
                "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
                "content": ''.join(vanit),
            }
            requests.post(url=wurl, data=payload)        
        else:
            funni = round(len(vanit)/20)
            for i in range(funni):
                payload = {
                    "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
                    "content": ''.join(vanit[i*20:i*20+20]),
                }
                requests.post(url=wurl, data=payload)
                time.sleep(1)
    elif how == 't':
        f = open(filen,'w+')
        f.write(''.join(vanit))
        f.close()

def proxy(reps):
    if reps <= 19:
        pass
    else:
        for i in range(reps):
            asyncio.run(main())
            time.sleep(60*10)
        
def starta():
    global min, max, repeat
    print('Starting')
    asyncio.run(main())
    time.sleep(.5)
    
    t1 = threading.Thread(target=proxy(repeat))
    t1.start
    t2 = threading.Thread(target=vanity(min,max,repeat))
    t2.start()


def startb():
    global filep, min, max, repeat, working
    print('Starting')
    f = open(filep).read()
    working = f.splitlines()
    t2 = threading.Thread(target=vanity(min,max,repeat))
    t2.start()
    
min = int(input('min letters: '))
max = int(input('max letters: '))
repeat = int(input('# of times to repeat: '))
how = input('webhook (w) or txt file (t): ')
if how == 'w':
    wurl = input('webhook url: ')
elif how == 't':
    filen = input('filepath to text file (include the .txt): ')
sow = input('use built in proxy scraper (b) or use a proxy list (.txt) (p): ')
if sow == 'b':
    starta()
if sow == 'p':
    filep = input('filepath to proxy list (http proxies in a .txt file, include the .txt): ')
    startb()