#description Sets log channel - Takes Channel ID

import discord
from discord import errors
from utils import utils
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

options = [
    {
        'name': 'channelID',
        'description': 'ChannelID to set for all logging output',
        'required': True,
        'type': 7
    }
]

class set_chn_log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(pass_context=True)
    #@commands.has_permissions(kick_members=True)
    #@commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @cog_ext.cog_slash(name='set_chn_log', description='Set channel for logging', guild_ids=[757508676784488559], options=options)
    async def set_chn_log(self, ctx: SlashContext, chn):
        try:
            channel = await self.bot.fetch_channel(int(chn.id))
            utils.modify_settings('chn_log', chn.id)
            await ctx.respond()
        except errors.NotFound:
            await ctx.channel.send('Channel not found')

        #await ctx.message.delete()

def setup(bot):
    bot.add_cog(set_chn_log(bot))