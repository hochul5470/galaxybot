import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
import urllib.parse, urllib.request, re
import urllib
import time
from urllib import request
from discord import guild, member, user
import os
import json
from Dtime import Uptime

async def bt(games):
    await bot.wait_until_ready()

    while not bot.is_closed():
        for g in games:
            await bot.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)

Uptime.uptimeset()

calcResult = 0

@bot.event
async def on_ready():
    print("team.DBMAH GALAXY BOT 봇")
    await bt(["GALAXY BOT 입니다! (made by 호철Hochul)", "본 메시지는 10초에 1번씩 봐꿔저요!", "?명령어를 이용해 명령어 확인해주세요!", "http://dbmah.na.to"])
    await asyncio.sleep(86400)
    os.system("start main_discord_bot.py")

@bot.command(name="활성화")
async def load(ctx, extension):
    bot.load_extension('활성화 완료')

@bot.command(name="비활성화")
async def unload(ctx, extension):
    bot.unload_extension(f'비활성화 완료')

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


token = os.environ.get("TOKEN")
bot.remove_command("help")
bot.run(token)
