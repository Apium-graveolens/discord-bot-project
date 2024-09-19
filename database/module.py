import discord
from discord import Embed

forbidden_word = ["花椰菜", "包心菜", "狡猾", "素", "gay", "9@y"]

first_embed = discord.Embed(title='Ninomae Ina\'nis',
                            url='https://www.youtube.com/@NinomaeInanis',
                            description='Ina\'s channel')


raf_twitch=discord.Embed(title='**拉福 - Twitch**',
                         url='https://www.twitch.tv/rafu191',
                         description='拉福 streams live on Twitch! Check out their videos, sign up to chat, and join their community.')
raf_twitch.set_author(name='Twitch')
raf_twitch.set_thumbnail(url='https://static-cdn.jtvnw.net/jtv_user_pictures/4c155611-ff13-414a-ad61-a88f9b827623-profile_image-300x300.png')
