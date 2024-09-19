import truststore
truststore.inject_into_ssl()

import database.module as module
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client
from discord.ext import commands

#
# LOAD TOKEN
#
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#
# BOT SETUP
#
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
bot: Client = commands.Bot(command_prefix = '%', intents=intents)

#
# COGS LOAD COMMANDS
#
@bot.command()
async def load(ctx, extension: str):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"[{extension}] loaded successfully")

@bot.command()
async def unload(ctx, extension: str):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"[{extension}] unloaded successfully")

@bot.command()
async def reload(ctx, extension: str):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"[{extension}] reloaded successfully")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"file [{filename}] loaded")

#
# START UP
#
@bot.event
async def on_ready() -> None:
    try:
        await load_extensions()
    except Exception as e:
        print(e)

    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    
    print(f"{bot.user} is now running")


#
# MAIN ENTRY POINT
#
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
