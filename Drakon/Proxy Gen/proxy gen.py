import os
import random
try:
    import discord
    from discord.ext import commands
    import discord.utils
    import 
except:
    os.system('pip install discord DiscordUtils pystyle')
    import discord
    from discord.ext import commands
    import discord.utils
    from pystyle import Colorate, Colors, Center
    
### IMPORTANT ###

### PUT YOUR DISCORD BOT'S TOKEN HERE ###

token = 'token'

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
                                                                                              
  _ \                                  ___|             
 |   |  __|   _ \   \  /  |   |       |      _ \  __ \  
 ___/  |     (   |    <   |   |       |   |  __/  |   | 
_|    _|    \___/  _/\_\ \__. |      \____|\___| _|  _| 
                         ____/                          

Created By FreeShit ║ getfreeshit.today 


""",1))

### -------------------------- ###

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all(), help_command=None)

users = []

def funny():
    global users
    try:
        with open('info.txt','r') as f:
            text = f.read()
            text = text.splitlines()
            for line in text:
                wee = line.split(':')
                hola = str(wee[0])
                we = int(wee[1])
                users.append([hola,we])
    except:
        pass
    
            
funny()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('with your mom'))
        
@bot.command()
async def help(ctx):
    await ctx.send('!send <user mention> <amount>, !bal, !shutdown, !save, !work, !remove <user mention> < amount>, !lb')
    
@bot.command()
async def send(ctx, usor: discord.Member, amount: int):
    global users
    sender = str(ctx.message.author.name) + '#' + str(ctx.message.author.discriminator)
    reciever = str(usor.name) + '#' + str(usor.discriminator)
    num = None
    if discord.utils.get(ctx.guild.roles, name = "Admin") in ctx.message.author.roles:
        for user in users:
            try:
                num = user.index(reciever)
                num = users.index(user)
            except:
                pass
        if num is None:
            users.append([reciever,amount])
            await ctx.send(f'{usor.mention}, {ctx.message.author.name} just sent you [**{amount}**]')
        else:
            users[num][1] = users[num][1] + amount
            await ctx.send(f'{usor.mention}, {ctx.message.author.name} just sent you [**{amount}**]')
    else:
        for user in users:
            try:
                num = user.index(sender)
                num = users.index(users)
            except:
                pass
        if num is None:
            await ctx.send('you got no cash to be sending broke mf')
        else:
            for user in users:
                try:
                    nom = user.index(reciever)
                    nom = users.index(user)
                except:
                    pass
            if nom is None:
                users.append([reciever,amount])
                users[num][1] = users[num][1] - amount
                await ctx.send(f'{usor.mention}, {ctx.message.author.name} just sent you [**{amount}**]')
            else:
                users[nom][1] = users[nom][1] + amount
                users[num][1] = users[num][1] - amount
                await ctx.send(f'{usor.mention}, {ctx.message.author.name} just sent you [**{amount}**]')
    
@bot.command()
async def remove(ctx, usor: discord.Member, amount: int):
    global users
    asshole = str(ctx.message.author.name) + '#' + str(ctx.message.author.discriminator)
    bozo = str(usor.name) + '#' + str(usor.discriminator)
    num = None
    if discord.utils.get(ctx.guild.roles, name = "Admin") in ctx.message.author.roles:
        for user in users:
            try:
                num = user.index(bozo)
                num = users.index(user)
            except:
                pass
            if num is None:
                pass
            else:
                if amount > users[num][1]:
                    users[num][1] = 0
                else:
                    users[num][1] = users[num][1] - amount
    else:
        pass    
    
                
@bot.command()
async def work(ctx):
    global users
    fun = ctx.message.author.name + '#' + ctx.message.author.discriminator
    cash = random.randint(10,100)
    num = None
    if ctx.channel.name != 'work':
        pass
    else:
        for user in users:
            try:
                num = user.index(fun)
                num = users.index(user)
            except:
                pass
    if num is None:
        users.append([fun,cash])
        await ctx.send(f'you just earned[**{cash}**]')
    else:
        users[num][1] = users[num][1] + cash
        await ctx.send(f'you just earned [**{cash}**] dollars')
                        
@bot.command()
async def shutdown(ctx):
    global users
    text = ''
    for user in users:
        text = text + f'\n{user[0]}:{user[1]}'
    final = ''.join(text.splitlines(keepends=True)[1:])
    with open('info.txt','w+') as f:
        f.write(final)
        f.close()    
        exit()
    
@bot.command()
async def save(ctx):
    global users
    text = ''
    for user in user:
        text = text + f'\n{user[0]}:{user[1]}'
    final = ''.join(text.splitlines(keepends=True)[1:])
    with open('info.txt','w+') as f:
        f.write(final)
        f.close()
        
@bot.command()
async def bal(ctx):
    global users
    num = None
    fun = ctx.message.author.name + '#' + ctx.message.author.discriminator
    for user in users:
        try:
            num = user.index(fun)
            num = users.index(user)
        except:
            pass
    if num is None:
        await ctx.send('you got no cash you broke ass bitch')
    else:
        await ctx.send(f'you got [**{users[num][1]}**] dollars')

    
@bot.command()
async def lb(ctx):
    userlist = []
    for user in users:
        userlist.append(user)
    biguser = userlist[0][1]
    topten = []
    num = None
    if len(userlist) >= 10:
        for i in range(10):
            for user in userlist:
                if user[1] > biguser:
                    biguser = user[1]
                    num = userlist.index(user)
                else:
                    num = userlist.index(user)
            topten.append(userlist[num])
            del userlist[num]
    else:
        for i in range(len(userlist)):
            for user in userlist:
                if user[1] > biguser:
                    biguser = user[1]
                    num = userlist.index(user)
                else:
                    num = userlist.index(user)
            topten.append(userlist[num])
            del userlist[num]
    embed = discord.Embed(title = 'Top Ten')
    for iteem in topten:
        iteem.reverse()
    topten.sort(reverse=True)
    for user in topten:
        nom = topten.index(user) + 1
        embed.add_field(name = f'#{nom} - [**{user[1]}**]',value = f'{user[1]} has [**{user[0]}**] dollars',inline = False)
    await ctx.send(embed=embed)
    for iteem in topten:
        iteem.reverse()
    topten.sort(reverse=True)
        
bot.run(token)