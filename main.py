import discord
from discord.ext import commands
import json
import requests
import random
import os
from bs4 import BeautifulSoup
from discord import Embed
import keep_alive


with open('setting.json', mode='r', encoding='UTF8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("啟動")
    # channel = bot.get_channel(int(jdata['online']))
    # await channel.send('機器人以上線')
@bot.command()
async def reload(ctx, extension):
    await ctx.message.delete()
    bot.reload_extension(f'discordbot.{extension}')

for filename in os.listdir('./discordbot'):
    if filename.endswith('.py'):
        bot.load_extension(f'discordbot.{filename[:-3]}')
    
#{代號.select_one("span").getText()}

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['token'])