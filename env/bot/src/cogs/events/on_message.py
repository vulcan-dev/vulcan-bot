import discord
from discord.ext import commands
from discord import errors
from utils import utils

class on_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            utils.logger.info(f'Message {{Name: {message.author.name}, Content: {message.content}, Channel: {message.channel}}}')
        except Exception as e:
            utils.logger.warning(e)
    
def setup(bot):
    bot.add_cog(on_message(bot))