import disnake, config, os, asyncio
from disnake.ext import commands, tasks
from disnake.ext.commands import slash_command
import random
import time
from colorama import Fore
from javascript import require, On, Once, AsyncTask, once, off
def banner():
    print(f"{Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗ ")
    time.sleep(0.2)
    print(f"{Fore.BLUE}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝ ")   
    time.sleep(0.2)
    print(f"{Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║    ")   
    time.sleep(0.2)
    print(f"{Fore.BLUE}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    ") 
    time.sleep(0.2)  
    print(f"{Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║    ")   
    time.sleep(0.2)
    print(f"{Fore.BLUE}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    ") 
    time.sleep(0.2)  
    print(f"{Fore.RED}Created By FreeShit ║ getfreeshit.today") 
    print(f"{Fore.WHITE}")

FreeShitMineFlayer = require('mineflayer')

bot = commands.Bot(
  command_prefix="FS!",
  intents=disnake.Intents.all(),
  help_command=None
)
banner()

@bot.slash_command(description="Help Menu")
async def help(interaction):
    embed=disnake.Embed(title="Help Menu", description="The help menu to guide you how to use FreeShit Bot")
    embed.add_field(name="Cracked Botter", value="FS! or /cracked <ip> <port> <username> <bot count>", inline=False)
    embed.add_field(name="Microsoft Botter", value="FS! or /microsoft <ip> <port> <username> <password>", inline=False)
    embed.add_field(name="Help", value="FS! or /Help", inline=False)
    await interaction.send(embed=embed)
    await bot.get_slash_command("help").callback(interaction)

@bot.slash_command(description="Microsoft Server Botter")
@commands.has_role('owner')
async def microsoft(interaction, ip: str, port: str, username: str, password: str):
    bot = FreeShitMineFlayer.createBot({'auth': 'microsoft', 'host': ip, 'port': port, 'username': username, 'password': password, 'hideErrors': False })
    await interaction.send("[Successful] Sent Account to that server " + str(ip)  + ":" + str(port))
    await bot.get_slash_command("microsoft").callback(interaction)
    

@bot.slash_command(description="Cracked Server Botter")
@commands.has_role('owner')
async def cracked(interaction, server: str, port: str,name: str, amount: str):
    for x in range(int(amount)):
            cock = name + "_" + str(random.randint(1, 9999))
            bot = FreeShitMineFlayer.createBot({'auth': 'cracked', 'host': str(server), 'port': str(port), 'username': cock})
            print(cock + " Has Joined")
    embed=disnake.Embed(title="Cracked Info", description="Cracked Server Botter Info")
    embed.add_field(name="Server IP:", value=f"{server}", inline=False)
    embed.add_field(name="Server Port:", value=f"{port}", inline=False)
    embed.add_field(name="Bot Usernames:", value=f"{name}", inline=False)
    embed.add_field(name="Bot Amount Sent:", value=f"{amount}", inline=False)
    embed.add_field(name="Status:", value=f"Bots Have Been Sent Successfully", inline=False)
    await interaction.send(embed=embed)
    await bot.get_slash_command("cracked").callback(interaction)



bot.run('')    
