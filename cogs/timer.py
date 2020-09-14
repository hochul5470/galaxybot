import asyncio
import discord
from discord.ext import commands
import os

class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="타이머")
    async def timer(self, ctx, mins):
        current_nick = ctx.author.nick
        await ctx.send(f"{ctx.author.mention} 님께서 {mins}분 타이머 설정 하셨습니다. 지금부터 {mins}분의 타이머가 돌아갑니다!")

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.send(f"{ctx.author.mention} 타이머 {mins}분이 끝났습니다!")
                break

def setup(bot):
    bot.add_cog(Play(bot))