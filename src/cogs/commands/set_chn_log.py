#description Sets log channel - Takes Channel ID

import discord
from discord import errors
from utils import utils
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class set_chn_log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(pass_context=True)
    #@commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def set_chn_log(self, ctx: SlashContext, chn):
        try:
            channel = await self.bot.fetch_channel(int(chn))
            utils.modify_settings('chn_log', chn)
            await ctx.message.channel.send(f'Successfully set log channel to: {channel.mention}')
        except errors.NotFound:
            await ctx.message.channel.send('Channel not found')

        await ctx.message.delete()

def setup(bot):
    bot.add_cog(set_chn_log(bot))