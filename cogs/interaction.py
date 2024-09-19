from discord.ext import commands
from discord import app_commands
from typing import Optional
import random
import discord



class interaction(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = "hello")
    async def hello(self, interaction: discord.Integration):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command")
    
    @app_commands.command(name = "create_embed")
    async def create_embed(self, interaction: discord.Integration, title: str, url: Optional[str], description: str):
        await interaction.response.send_message(embed= discord.Embed(title= title, url= url, description= description))
    
    @app_commands.command(name = "roll_dice")
    async def roll_dice(self, interaction: discord.Integration):
        await interaction.response.send_message(f"You got {random.randint(1, 6)} point")

    @app_commands.command(name = "flip_a_coin")
    async def flip_a_coin(self, interaction: discord.Integration):
        if random.randint(0, 1):
            await interaction.response.send_message(f"You got Heads")
        else:
            await interaction.response.send_message(f"You got Tails")

    

async def setup(bot: commands.Bot):
    await bot.add_cog(interaction(bot))