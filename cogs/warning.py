import discord
from discord.ext import commands
import asyncio
import pickle

my_variable =  1
with open("data/warming.bin", "wb+") as f:
    pickle.dump(my_variable, f)


class Admin(commands.Cog, name="관리자"):

    """
    관리자 명령어들입니다.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="경고",
                  usage="!경고 [유저 태그] [경고 횟수]")
    @commands.has_permissions(administrator=True)
    async def give_warning(self, ctx, user_name: discord.Member, amount: int=1):
        try:
            with open("data/warning.bin", "rb") as f:
                warning_data = pickle.load(f) 
        except FileNotFoundError: 
            with open("data/warning.bin", "wb+") as f:
                warning_data = dict()
                pickle.dump(warning_data, f)

        if str(user_name.id) not in warning_data: 
            warning_data[str(user_name.id)] = amount 
        else: 
            warning_data[str(user_name.id)] += amount 

        with open("data/warning.bin", "wb") as f:
            pickle.dump(warning_data, f)

        embed = discord.Embed(title="🚨경고가 추가되였습니다🚨",
                              description=f"{user_name.mention}님에게 경고가 부여되었습니다.\n경고 횟수: {amount}\n처리 관리자 : {ctx.author.mention}",
                              color=0xFF0000)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
