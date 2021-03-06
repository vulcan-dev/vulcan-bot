import discord
from discord.ext import commands
from discord import errors
from utils import utils

class on_message_delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            embed=discord.Embed(description=f'Message sent by {message.author.mention} deleted in {message.channel.mention}', color=0xff0000)
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.add_field(name="Content", value=message.content)
            embed.set_footer(text=utils.get_time())

            channel = await self.bot.fetch_channel(int(utils.load_settings()['chn_log']))
            await channel.send(embed=embed)
        except errors.HTTPException:
            pass

def setup(bot):
    bot.add_cog(on_message_delete(bot))