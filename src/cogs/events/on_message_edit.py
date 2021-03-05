import discord
from discord.ext import commands
from discord import errors
from utils import utils

# Sends, deletes, tries to send again, error is caught so it doesn't continue
class on_message_edit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            embed = discord.Embed(description=f'Message sent by {before.author.mention} edited in {before.channel.mention}', color=0xff5900)
            embed.set_author(name=before.author, icon_url=before.author.avatar_url)
            embed.add_field(name="Before", value=f'{before.content}', inline=False)
            embed.add_field(name="After", value=f'{after.content}', inline=False)
            embed.set_footer(text=utils.get_time())

            channel = await self.bot.fetch_channel(int(utils.load_settings()['chn_log']))
            await channel.send(embed=embed)
        except errors.HTTPException:
            pass
    
def setup(bot):
    bot.add_cog(on_message_edit(bot))