#description Sets rules channel - Takes Channel ID

import discord
from discord.ext import commands
from discord import errors
from utils import utils
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

options = [
    {
        'name': 'channelID',
        'description': 'The ID of the rules channel',
        'required': True,
        'type': 7
    }
]

class set_chn_rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @cog_ext.cog_slash(name='set_chn_rules', description='Set channel for the rules', guild_ids=[757508676784488559], options=options)
    async def set_chn_rules(self, ctx: SlashContext, chn):
        try:
            channel = await self.bot.fetch_channel(int(chn.id))
            utils.modify_settings('chn_rules', chn.id)
            await ctx.respond()
        except errors.NotFound:
            await ctx.respond()
            await ctx.channel.send('Channel not found')

def setup(bot):
    bot.add_cog(set_chn_rules(bot))