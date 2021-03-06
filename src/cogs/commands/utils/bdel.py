#description Bulk deleted messages - Takes count
#description Deletes message(s) - Takes amount of messages to be deleted

import asyncio
from discord.ext import commands
from discord.ext.commands.core import check
from utils import utils
from bot import slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

options = [
    {
        'name': 'x',
        'description': 'Messages to delete',
        'required': True,
        'type': 4
    }
]

class bdel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @cog_ext.cog_slash(name='bdel', description='Deletes x messages', guild_ids=[757508676784488559], options=options)
    async def bdel(self, ctx: SlashContext, amount):
        def not_pinned(msg): return not msg.pinned
        try:
            await ctx.respond()
            await ctx.channel.purge(limit=int(amount), check=not_pinned)
        except Exception as e: print(e)

def setup(bot):
    bot.add_cog(bdel(bot))