import requests,os
from time import sleep as sleep
from platform import system as psystem
__version__ = "1.0.0"
banner = """
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
Created By FreeShit ║ Dev: Minkenderslapvæk#6760 ║ getfreeshit.today
                      Version {}
""".format(__version__)
print(banner)

def clear():
    co = psystem()
    if co == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    try:
        channel_id = input("Channel ID: ")
        discord_token = input("Discord Token: ")
        message = input("Message to spam: ")
        amount = int(input("Amount of message(s): "))
    except ValueError:
        print("A input field, was given the wrong information.. exiting...")
        exit(1)
    except:
        print("Something went wrong (buffer overflow?).. exiting...")
        exit(1)
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    r_headers = {
    'Authorization': discord_token,
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    r_data = "content={}".format(message)
    for x in range(amount+1):
      response = requests.post(url, headers=r_headers, data=r_data)
      respjson = response.json()

      if response.status_code == 200:
          pass
      elif response.status_code == 404:
          print("Not a channel ID (User ID?)")
          exit(1)
      try:
        if respjson["code"] == 20028:
            print("Waiting {} seconds.".format(respjson["retry_after"]))
            sleep(response.json()["retry_after"])
      except KeyError:
        pass

if __name__ == "__main__":
    main()


#1041412889086525463 - Channel ID
#993586067234099262 - User ID