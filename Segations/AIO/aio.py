import os,colorama,requests,time,string,random,threading,json
from colorama import init,Fore
from time import sleep
from rich.console import Console
from rich.markdown import Markdown

color = colorama.Fore

init()
banner = f"""
{colorama.Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗     █████╗ ██╗ ██████╗ 
{colorama.Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝    ██╔══██╗██║██╔═══██╗
{colorama.Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║       ███████║██║██║   ██║
{colorama.Fore.GREEN}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║       ██╔══██║██║██║   ██║
{colorama.Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║       ██║  ██║██║╚██████╔╝
{colorama.Fore.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝ ╚═════╝ 
{colorama.Fore.RED}Created By FreeShit ║ Dev: segations#2344 ║ getfreeshit.today
{colorama.Fore.GREEN}                      Version 1.1.3
"""
def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def info():
    print(colorama.Fore.RED + "I Got Bored and decided to create a paste spammer for most of the Pastebin alternatives")
    print(colorama.Fore.RED + "This Was Made by Segation using, http toolkit, burp suite, chrome, curlconverter.com")
    sleep(10)
    os.system("cls")
    menu()


def dpastecom():
    message = input("Message >> ")
    amount = int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    f = open("dpastecom.txt", "a")
    os.system("title DPaste.com ║ message: {} ║ Amount: {} ║ Threading: {}".format(message, amount, user_threads))    
    def spammer():
        cookies = {
            'csrftoken': 'KXLguvvFWf1EuvnquVzdp4Wxock4Hz0CZ2xeDPIh3NKZs0XE7pPS1COvizvhD8jD',
        }

        headers = {
            'authority': 'dpaste.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'csrftoken=KXLguvvFWf1EuvnquVzdp4Wxock4Hz0CZ2xeDPIh3NKZs0XE7pPS1COvizvhD8jD',
            'origin': 'https://dpaste.org',
            'referer': 'https://dpaste.org/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        data = {
            'csrfmiddlewaretoken': 'je1GTSdL67NnIaIG8nmgq2gB3S2h9DaRyjNE2cqndFwIGFiULRCV2A8zXfdu5ctS',
            'title': '',
            'lexer': 'python',
            'expires': '31536000',
            'content': 'print("{}")'.format(message),
        }

        for x in range(amount):
            r = requests.post('https://dpaste.org/', cookies=cookies, headers=headers, data=data)
            print(colorama.Fore.RED + r.url + colorama.Fore.GREEN + " - [SuccessFul]" + colorama.Fore.WHITE)
            f.write(r.url+ "\n")
            
            
    threads = []
    def main(user_threads):
            try:
                for i in range(user_threads):
                    thread = threading.Thread(target=spammer, daemon=True)
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

def dpaste():
    
    print(color.RED + "You Have Selected DPaste Spammer")
    os.system("title DPaste.org Spammer")
    f = open("dpasteorg.txt", "a")

    message = input("Whats The Message >> ")
    amount = int(input("How Many Pastes >> "))
    os.system("title DPaste.org ║ message: {} ║ Amount: {}".format(message, amount))
    i = 0
    for x in range(amount):
        i += 1
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'https://dpaste.com',
            'Referer': 'https://dpaste.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.127 Chrome/10.0.648.127 Safari/534.16',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = {
            'content': f'print("{message}")',
            'syntax': 'python',
            'title': get_random_string(10),
            'expiry_days': '365',
        }
        sleep(0.6)
        response = requests.post('https://dpaste.com/', headers=headers, data=data)
        print(colorama.Fore.RED + response.url + colorama.Fore.GREEN + " - [SuccessFul]" + colorama.Fore.WHITE)
        f.write(response.url+ "\n")
def exobin():
    os.system("title ExoBin.cf Spammer")
    user_threads = int(input("How Many Threads >> "))
    messages = input("Message >> ")
    amount = int(input("How Many >> "))
    os.system("title ExoBin.cf ║ message: {} ║ Amount: {} ║ Threads: {}".format(messages, amount, user_threads))
    f = open("exobin.txt", "a")

    def exobindo():
        i = 0
        for x in range(amount):
            i += 1
            data = {
                'data': messages
            }
            r= requests.post('https://exobin.cf/new.php', data=data)
            if r.status_code == 200: 
                print(colorama.Fore.RED + r.url + colorama.Fore.GREEN + " - [SuccessFul]" + colorama.Fore.WHITE)
                f.write(r.url + "\n")
            else: 
                print("Failed. " + str(r.status_code))

    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=exobindo, daemon=True)
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
def friendpaste():
    os.system("title friendpaste.com Spammer")
    f = open("friendpaste.txt", "a")
    title = input("Title >> ")
    text = input("Text >> ")
    amount = int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    os.system("title friendpaste.com ║ Title: {} ║ Text: {} ║ Amount: {} ║ Threads: {}".format(title,text,amount,user_threads))

    def spammer():

        cookies = {
            'FRIENDPASTE_SID': '505c149153db376d415e90285859d6462b76a21f',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'https://friendpaste.com',
            'Referer': 'https://friendpaste.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'paste-snippet': text,
            'paste-language': 'python',
            'paste-title': title,
            'paste-code': '',
            'paste-privacy': 'open',
            'paste-password': '',
            'psubmit': 'Submit post',
        }

        for x in range(amount):
            response = requests.post('https://friendpaste.com/', cookies=cookies, headers=headers, data=data)
            print(colorama.Fore.RED + response.url + colorama.Fore.GREEN + " - [SuccessFul]" + colorama.Fore.WHITE)
            f.write(response.url + "\n")
            
    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=spammer, daemon=True)
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

def glotio():
    os.system("title glot.io Spammer")
    title = input("Title >> ")
    name = input("Name of file >> ")
    message = input("Message >> ")
    amount = int(input("Amount of pastes (this will be times by the threads so this x by threads) >> "))
    user_threads = int(input("Threads >> "))
    
    os.system("title glot.io ║ Title: {} ║ Name: {} ║ Message: {} ║ Amount: {} ║ Threads: {}".format(title,name,message,amount,user_threads))
    
    url = "https://glot.io/new/python?version=latest&command=&stdin="

    f = open("glotio.txt", "a")


    def glotiospammer():
        for x in range(amount):
            
            payload = json.dumps({
            "language": "python",
            "title": title + '_getfreeshit.today_' + get_random_string(3),
            "public": True,
            "files": [
                {
                "name": "{}.py".format(name),
                "content": "print(\"{}\")\n# Made By FreeShit Spammer\n# https://getfreeshit.today/".format(message)
                }
            ]
            })
            
            
            headers = {
            'Content-Type': 'application/json',
            }

            r = requests.post(url, headers=headers,data=payload)
            
            power = r.text.replace('"', '')
            insane = power.replace(':','')
            wow = insane.replace("url", '')
            happy = wow.replace("{",'')
            cope = happy.replace("}",'')
            fewbi = cope.replace("https//",'')
            print("https://" + fewbi  + " - Created Successfully")
            f.write("https://" + fewbi + "\n")

    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=glotiospammer, daemon=True)
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
def klgrth():
    os.system("title klgrth.io Spammer")
    f = open("klgrth.txt", "a")

    text = input("Text >> ")
    amount = int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    os.system("title klgrth.io ║ Text: {} ║ Amount: {} ║ Threads: {}".format(text,amount,user_threads))

    def klgrthspammer():
        headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Origin': 'https://pst.klgrth.io',
                'Referer': 'https://pst.klgrth.io/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        for x in range(amount):
            data = {
                'lang': 'text',
                'text': f'{text}_{get_random_string(10)}',
                'expire': '-1',
                'password': '',
                'title': '',
            }

            response = requests.post('https://pst.klgrth.io/paste/new', headers=headers, data=data)
            print(colorama.Fore.RED + response.url + colorama.Fore.WHITE + " - " + colorama.Fore.GREEN + "[Successful]" + colorama.Fore.WHITE)
            f.write(response.url + "\n")

    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=klgrthspammer, daemon=True)
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
def paste():
    os.system("title paste.ee Spammer")
    f = open("pasteee.txt", "a")
    title=input("Title >> ")
    content=input("Content >> ")
    descriptions=input("Description >> ")
    amount=int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    os.system("title paste.ee ║ Title: {} ║ Content: {} ║ Description: {} ║ Amount: {} ║ Threads: {}".format(title,content,descriptions,amount,user_threads))
    headers = {
        'Host': 'paste.ee',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://paste.ee',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://paste.ee/',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    def pastespammer():
        for x in range(amount):
            data = { # 40
                '_token': get_random_string(40),
                'expiration': '31536000',
                'expiration_views': '',
                'description': descriptions,
                'paste[section1][name]': title,
                'paste[section1][syntax]': 'text',
                'paste[section1][contents]': content,
                'fixlines': 'true',
                'jscheck': 'validated',
            }

            r = requests.post('https://paste.ee/paste', headers=headers, data=data)
            print(colorama.Fore.RED + r.url + colorama.Fore.WHITE+" - " + colorama.Fore.GREEN+ "[Successful]")
            f.write(r.url+ "\n")
            
    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=pastespammer, daemon=True)
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
def pastelink():
    os.system("title pastelink.net Spammer")
    f = open("pastelink.txt", "a")
    title = input("Title >> ")
    message = input("Message >> ")
    amount = int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    os.system("title pastelink.net ║ Title: {} ║ Message: {} ║ Amount: {} ║ Threads: {}".format(title,message,amount,user_threads))


    def pastelinkspammer():

        
        headers = {
            'authority': 'pastelink.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'PHPSESSID=nm3183fdohju0k5if9hk0etmd3',
            'origin': 'https://pastelink.net',
            'referer': 'https://pastelink.net/submit',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        data = {
            'title': title,
            'font_name': 'Poppins',
            'font_weight': '400',
            'font_size': '16',
            'data-font-family': 'Poppins',
            'data-font-size': '16',
            'data-font-weight': '400',
            'body_raw': message,
            'visibility': 'public',
            'visibility_password': '',
            'expiry': '0',
            'expiry_number': '12',
            'expiry_qualifier': 'hours',
            'passcode': '',
            'link_options': 'show',
            'security': 'none',
            'referrer': 'public',
            'stripped': '0',
            'custom': '',
            'submit': 'Publish',
        }
        for x in range(amount):
            response = requests.post('https://pastelink.net/submit', headers=headers, data=data)
            print(colorama.Fore.RED + response.url + colorama.Fore.GREEN + " - [SuccessFul]" + colorama.Fore.WHITE)
            f.write(response.url + "\n")
    
    threads = []
    def main(user_threads):
                try:
                    for i in range(user_threads):
                        thread = threading.Thread(target=pastelinkspammer, daemon=True)
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

def sandboxgl():
    os.system("title glslsandbox.com Spammer")
    amount = int(input("Amount >> "))
    user_threads = int(input("Threads >> "))
    
    os.system("title glslsandbox.com ║ Amount: {} ║ Threads: {}".format(amount,user_threads))
    def spammer():

        headers = {
            'authority': 'glslsandbox.com',
            'accept': 'text/plain, */*; q=0.01',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '__e_inc=1',
            'origin': 'https://glslsandbox.com',
            'referer': 'https://glslsandbox.com/e',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '{"code":"\\n#ifdef GL_ES\\nprecision highp float;\\n#endif\\n\\n// ↙\\n//  ↙\\n//   ↙\\n// http://66.media.tumblr.com/2a2f183dc4a6a040ff65355418b9403/tumblr_ncbj5rJvLI1tmxmpzo1_500.jpg\\n\\nvec2 uv;\\n\\nuniform float time;\\nuniform vec2 resolution;\\n\\nconst vec2 ch_size  = vec2(1.0, 2.0) * 0.6;              // character size (Y,X)\\nconst vec2 ch_space = ch_size + vec2(1.0, 1.0);    // character distance Vector(X,Y)\\nconst vec2 ch_start = vec2 (ch_space.x * -1.75, 3.25); // start position\\n      vec2 ch_pos   = vec2 (0.0, 0.0);             // character position(X,Y)\\n//      vec3 ch_color = vec3 (1.5, 0.75, 0.5);        // character color (R,G,B)\\n//const vec3 bg_color = vec3 (0.2, 0.2, 0.2);        // background color (R,G,B)\\n\\n#define REPEAT_SIGN false // True/False; True=Multiple, False=Single\\n\\n/* 16 segment display...Akin to LED Display.\\n\\nSegment bit positions:\\n  __2__ __14__\\n |\\\\    |    /|\\n | \\\\   |   / |\\n 5  11 40 9  0\\n |   \\\\ | /   |\\n |    \\\\|/    |\\n  _12__ __8__\\n |           |\\n |    /|\\\\    |\\n 4   / | \\\\   7\\n | 13 1  15 |\\n | /   |   \\\\ |\\n  __3__|__6__\\n\\n15 12 11 8 7  4 3  0\\n |  | |  | |  | |  |\\n 0000 0000 0000 0000\\n10101010101010101011\\n\\nexample: letter A\\n\\n   12    8 7  4 3210\\n    |    | |  | ||||\\n 0001 0001 1001 1111\\n\\n binary to hex -> 0x119F\\n*/\\n\\n#define n0 ddigit(0x22FF);\\n#define n1 ddigit(0x0281);\\n#define n2 ddigit(0x1177);\\n#define n3 ddigit(0x11E7);\\n#define n4 ddigit(0x5508);\\n#define n5 ddigit(0x11EE);\\n#define n6 ddigit(0x11FE);\\n#define n7 ddigit(0x2206);\\n#define n8 ddigit(0x11FF);\\n#define n9 ddigit(0x11EF);\\n\\n#define A ddigit(0x119F);\\n#define B ddigit(0x927E);\\n#define C ddigit(0x007E);\\n#define D ddigit(0x44E7);\\n#define E ddigit(0x107E);\\n#define F ddigit(0x101E);\\n#define G ddigit(0x807E);\\n#define H ddigit(0x1199);\\n#define I ddigit(0x4466);\\n#define J ddigit(0x4436);\\n#define K ddigit(0x9218);\\n#define L ddigit(0x0078);\\n#define M ddigit(0x0A99);\\n#define N ddigit(0x8899);\\n#define O ddigit(0x00FF);\\n#define P ddigit(0x111F);\\n#define Q ddigit(0x80FF);\\n#define R ddigit(0x911F);\\n#define S ddigit(0x8866);\\n#define T ddigit(0x4406);\\n#define U ddigit(0x00F9);\\n#define V ddigit(0x2218);\\n#define W ddigit(0xA099);\\n#define X ddigit(0xAA00);\\n#define Y ddigit(0x4A00);\\n#define Z ddigit(0x2266);\\n#define _ ch_pos.x += ch_space.x;\\n#define s_dot     ddigit(0);\\n#define s_minus   ddigit(0x1100);\\n#define s_plus    ddigit(0x5500);\\n#define s_greater ddigit(0x2800);\\n#define s_less    ddigit(0x8200);\\n#define s_sqrt    ddigit(0x0C02);\\n#define nl1 ch_pos = ch_start;  ch_pos.y -= 3.0;\\n#define nl2 ch_pos = ch_start;  ch_pos.y -= 6.0;\\n#define nl3 ch_pos = ch_start;\\tch_pos.y -= 9.0;\\n#define nl4 ch_pos = ch_start;\\tch_pos.y -= 12.0;\\n\\nfloat dseg(vec2 p0, vec2 p1)\\n{\\n\\tvec2 dir = normalize(p1 - p0);\\n\\tvec2 cp = (uv - ch_pos - p0) * mat2(dir.x, dir.y,-dir.y, dir.x);\\n\\treturn distance(cp, clamp(cp, vec2(0), vec2(distance(p0, p1), 0)));   \\n}\\n\\nbool bit(int n, int b)\\n{\\n\\treturn mod(floor(float(n) / exp2(floor(float(b)))), 2.0) != 0.0;\\n}\\n\\nfloat d = 1e6;\\n\\nvoid ddigit(int n)\\n{\\n\\tfloat v = 1e6;\\t\\n\\tvec2 cp = uv - ch_pos;\\n\\tif (n == 0)     v = min(v, dseg(vec2(-0.405, -1.000), vec2(-0.500, -1.000)));\\n\\tif (bit(n,  0)) v = min(v, dseg(vec2( 0.500,  0.063), vec2( 0.500,  0.937)));\\n\\tif (bit(n,  1)) v = min(v, dseg(vec2( 0.438,  1.000), vec2( 0.063,  1.000)));\\n\\tif (bit(n,  2)) v = min(v, dseg(vec2(-0.063,  1.000), vec2(-0.438,  1.000)));\\n\\tif (bit(n,  3)) v = min(v, dseg(vec2(-0.500,  0.937), vec2(-0.500,  0.062)));\\n\\tif (bit(n,  4)) v = min(v, dseg(vec2(-0.500, -0.063), vec2(-0.500, -0.938)));\\n\\tif (bit(n,  5)) v = min(v, dseg(vec2(-0.438, -1.000), vec2(-0.063, -1.000)));\\n\\tif (bit(n,  6)) v = min(v, dseg(vec2( 0.063, -1.000), vec2( 0.438, -1.000)));\\n\\tif (bit(n,  7)) v = min(v, dseg(vec2( 0.500, -0.938), vec2( 0.500, -0.063)));\\n\\tif (bit(n,  8)) v = min(v, dseg(vec2( 0.063,  0.000), vec2( 0.438, -0.000)));\\n\\tif (bit(n,  9)) v = min(v, dseg(vec2( 0.063,  0.063), vec2( 0.438,  0.938)));\\n\\tif (bit(n, 10)) v = min(v, dseg(vec2( 0.000,  0.063), vec2( 0.000,  0.937)));\\n\\tif (bit(n, 11)) v = min(v, dseg(vec2(-0.063,  0.063), vec2(-0.438,  0.938)));\\n\\tif (bit(n, 12)) v = min(v, dseg(vec2(-0.438,  0.000), vec2(-0.063, -0.000)));\\n\\tif (bit(n, 13)) v = min(v, dseg(vec2(-0.063, -0.063), vec2(-0.438, -0.938)));\\n\\tif (bit(n, 14)) v = min(v, dseg(vec2( 0.000, -0.938), vec2( 0.000, -0.063)));\\n\\tif (bit(n, 15)) v = min(v, dseg(vec2( 0.063, -0.063), vec2( 0.438, -0.938)));\\n\\tch_pos.x += ch_space.x;\\n\\td = min(d, v);\\n}\\nmat2 rotate(float a)\\n{\\n\\tfloat c = cos(a);\\n\\tfloat s = sin(a);\\n\\treturn mat2(c, s, -s, c);\\n}\\nvec3 hsv2rgb_smooth( in vec3 c )\\n{\\n    vec3 rgb = clamp( abs(mod(c.x*6.0+vec3(0.0,4.0,2.0),6.0)-3.0)-1.0, 0.0, 1.0 );\\n\\n\\trgb = rgb*rgb*(3.0-2.0*rgb); // cubic smoothing\\t\\n\\n\\treturn c.z * mix( vec3(1.0), rgb, c.y);\\n}\\nvoid main( void ) \\n{\\n\\t\\n\\tvec2 aspect = resolution.xy / resolution.y;\\n\\tuv = ( gl_FragCoord.xy / resolution.y ) - aspect / 2.0;\\n\\tfloat _d =  1.0-length(uv);\\n\\tuv *= 18.0 ;\\n\\tuv -= vec2(-7., 1.);\\n\\t//uv *= rotate(time+uv.x*0.05);\\n\\n\\tvec3 ch_color = hsv2rgb_smooth(vec3(time*0.4+uv.y*0.1,0.5,1.0));\\n\\n\\tvec3 bg_color = vec3(_d*0.4, _d*0.2, _d*0.1);\\n\\tuv.x += 0.5+sin(time+uv.y*0.7)*0.5;\\n\\tch_pos = ch_start;\\n\\n\\t\\n_ _ _ _ _ W O W _ nl1;\\n_ _ _ _  S O M E nl2;\\n_ _ _ _ T R O L L A G E nl3;\\n\\t      \\n                 \\n\\t\\t\\n\\tvec3 color = mix(ch_color, bg_color, 1.0- (0.08 / d*2.0));  // shading\\n\\tgl_FragColor = vec4(color, 1.0);\\n}","image":"data:image/gif;base64,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","user":"86c1542","parent":""}'.encode()

        for x in range(amount):
            response = requests.post('https://glslsandbox.com/e', headers=headers, data=data)
            print("Response Code: {} : Success".format(response.status_code))
            
    threads = []
    def main(user_threads):
                    try:
                        for i in range(user_threads):
                            thread = threading.Thread(target=spammer, daemon=True)
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

def other():
    os.system("title AIO ║ Current Selection: 1")
    print(banner)
    markdown_mainmenu = """
# Select the feature you want to use.
[G] Glslsandbox.com\n
[M] Menu"""

    console = Console()
    md = Markdown(markdown_mainmenu)
    console.print(md) 
    
    selection = input("\nWhat Feature >> ")
    
    if selection =="g" or selection=="G":
        sandboxgl()
        os.system("cls")
        spammerselection()
    if selection == "m" or selection=="M":
        os.system("cls")
        spammerselection()
    else:
        print("Not a Feature")
        sleep(2)
        other()

def spammerselection():
    os.system("title AIO ║ Current Selection: 2")
    print(banner)
    markdown_mainmenu = """
# Select the feature you want to use.
[P] PasteBin Alternatives\n
[F] Forums (Coming Soon)\n
[O] Other"""

    console = Console()
    md = Markdown(markdown_mainmenu)
    console.print(md) 
    
    selection = input("\nWhat Feature >> ")
    
    if selection == "P" or selection == "p":
        os.system("cls")
        spammer()
    if selection == "F" or selection == "f":
        print("Soon...")
        spammerselection()
    if selection == "o" or selection=="O":
        os.system("cls")
        other()
    else:
        print("Not a Feature")
        sleep(2)
        spammerselection()

def spammer():
    os.system("title AIO - PasteBin alternative Spammers ║ Current Websites: 8")
    print(banner)
    markdown_mainmenu = """
# Select the feature you want to use.
[C] Controlc.com (NOT FINISHED)\n
[D] Dpaste.com\n
[DP] Dpaste.org\n
[E] Exobin.cf\n
[F] FriendPaste.com\n
[G] Glot.io\n
[K] klgrth.io\n
[P] Paste.ee\n
[PA] PasteLink.net\n
[M] Menu"""

    console = Console()
    md = Markdown(markdown_mainmenu)
    console.print(md) 
    
    selection = input("\nWhat Feature >> ")
    
    if selection=="d" or selection=="D":
        os.system("cls")
        dpaste()
        os.system("cls")
        spammer()
    if selection=="dp" or selection=="DP":
        os.system("cls")
        dpastecom()
        os.system("cls")
        spammer()
    if selection=="e" or selection=="E":
        os.system("cls")
        exobin()
        os.system("cls")
        spammer()
    if selection=="f" or selection=="F":
        os.system("cls")
        friendpaste()
        os.system("cls")
        spammer()
    if selection=="g" or selection=="G":
        os.system("cls")
        glotio()
        os.system("cls")
        spammer()
    if selection=="k" or selection=="K":
        os.system("cls")
        klgrth()
        os.system("cls")
        spammer()
    if selection=="p" or selection=="P":
        os.system("cls")
        paste()
        os.system("cls")
        spammer()
    if selection=="pa" or selection=="PA":
        os.system("cls")
        pastelink()
        os.system("cls")
        spammer()
    if selection=="m" or selection=="M":
        os.system("cls")
        spammerselection()
    else:
        print("Not a Feature")
        sleep(2)
        spammer()


def menu():
    print(banner)
    markdown_mainmenu = """
# Select the feature you want to use.
[S] Spammer Shit\n
[I] Info Shit"""

    console = Console()
    md = Markdown(markdown_mainmenu)
    console.print(md) 
    os.system("title Select a Feature")

    selection = input("\nWhat Feature >> ")

    if selection=="S" or selection=="s":
        os.system("cls")
        spammerselection()
    if selection=="i" or selection=="I":
        os.system("cls")
        info()
    else:
        print("Not a Feature")
        sleep(2)
        menu()

menu()