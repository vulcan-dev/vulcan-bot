#description Sets welcome channel - Takes Channel ID

from discord.ext import commands
from discord import errors
from utils import utils

class set_chn_welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def set_chn_welcome(self, ctx, chn):
        try: 
            channel = await self.bot.fetch_channel(int(chn))
            utils.modify_settings('chn_welcome', chn)
            await ctx.message.channel.send(f'Successfully set welcome channel to: {channel.mention}')
        except errors.NotFound:
            await ctx.message.channel.send('Channel not found')

        await ctx.message.delete()

def setup(bot):
    bot.add_cog(set_chn_welcome(bot))