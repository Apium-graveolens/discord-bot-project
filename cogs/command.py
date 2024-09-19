from discord import Message, app_commands
from discord.ext import commands
import database.responses as responses
import database.module as module
import discord
import random


class command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # COMMANDS
    @commands.command()
    async def greeting(self, ctx):
        await ctx.send("Hello there!")
    
    @commands.command()
    async def time(self, ctx):
        await ctx.send(responses.get_localtime())
    
    @commands.command()
    async def ina(self, ctx):
        await ctx.send(embed = module.first_embed)

    @commands.command()
    async def raf(self, ctx):
        await ctx.send(responses.raf_response())

    @commands.command()
    async def raf_twitch(self, ctx):
        await ctx.send("https://www.twitch.tv/rafu191")
    
    @commands.command()
    async def penis(self, ctx):
        await ctx.send("8=====D")

    @commands.command()
    async def random_penis(self, ctx):
        string :str = "8"
        for i in range(random.randint(1, 50)):
            string += "="
        string += "D"
        await ctx.send(string)
    
    @commands.command()
    async def raf_penis(self, ctx):
        await ctx.send("8=D")


async def setup(bot: commands.Bot):
    await bot.add_cog(command(bot))