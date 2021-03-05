#description Sets rules channel - Takes Channel ID

import discord
from discord.ext import commands
from discord import errors
from utils import utils
from bot import slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

options = [
    {
        'name': 'channelID',
        'description': 'The ID of the log channel',
        'required': True,
        'type': 4
    }
]

class set_chn_rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @cog_ext.cog_slash(name='set_chn_rules', description='Sets log channel', guild_ids=[757508676784488559], options=options)
    async def set_chn_rules(self, ctx: SlashContext, channelID):
        print('working')
        try: 
            channel = await self.bot.fetch_channel(int(channelID))
            utils.modify_settings('chn_rules', channelID)
            await ctx.respond()
            await ctx.message.channel.send(f'Successfully set rules channel to: {channel.mention}')
        except errors.NotFound:
            await ctx.message.channel.send('Channel not found')

def setup(bot):
    bot.add_cog(set_chn_rules(bot))