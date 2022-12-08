import discord
import asyncio
import aiohttp
from discord.ext import commands
import requests
import os
import time

token = 'token'

bot = commands.Bot(command_prefix=",", self_bot=True, help_command=None)

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("selfbot has started")
    
@bot.command()
async def eping(ctx):
    await ctx.message.delete()
    guild = await bot.fetch_guild(ctx.guild.id)
    guild = bot.get_guild(ctx.guild.id)
    time.sleep(2)
    members = [m.mention for m in guild.members]
    if len(members) <= 20:
        funny = await ctx.send(''.join(members))
        await funny.edit(content = '@.everyone lol')
    else:
        funni = round(len(members)/20)
        for i in range(funni):
            funny = await ctx.send(''.join(members[i*20:i*20+20]))
            await funny.edit(content = '@.everyone lol')
            time.sleep(1)

@bot.command()
async def s(ctx):
    await ctx.message.delete()
    exit()
            
bot.run(token)