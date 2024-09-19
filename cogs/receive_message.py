from discord import Message
from discord.ext import commands
from database import responses, module

#
# MESSAGE FUNCTIONALITY
#
async def send_message(message: Message, user_message: str) -> None:
    if message.content.startswith('%'):
        await commands.process_commands(message)
        return

    if not user_message:
        print('Sth wrong')
        return
    if user_message == 'stop':
        response = 'i quit'
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

        await message.author.send(response) if is_private else await message.channel.send(response)
        quit()

    try:
        response: str = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)


class receive_message(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #
    # RECEIVE MESSAGE
    #
    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        print(f'[{message.channel}] {message.author}: "{message.content}"')
        if message.author == self.bot.user:
            return

        if message.content == "stop": # SHUT DOWN
            if str(message.author) == "apium_graveolens":
                await message.channel.send("sure")
                quit()
            else:
                await message.channel.send("Who do you think you are?")
    
        for word in module.forbidden_word: # DELETE FORBIDDEN_WORD
            if word.lower() in message.content.lower():
                await message.delete()
                return
        
        return 
        ## TMP SURPRESS
        if message.channel != '🎤command':
            print(f'is at [{channel}] channel')
            return
    
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)


async def setup(bot: commands.Bot):
    await bot.add_cog(receive_message(bot))