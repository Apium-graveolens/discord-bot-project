from discord.ext import commands
from googlesearch import search
from bs4 import BeautifulSoup
from discord import app_commands
from time import sleep
import discord

class google_search(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # COMMANDS
    @commands.command()
    async def search1(self, ctx, search_msg: str):
        for result in search(search_msg, stop=3):
            await ctx.send(embed= discord.Embed(title= result, url= result))
            sleep(0.5)


async def setup(bot: commands.Bot):
    await bot.add_cog(google_search(bot))