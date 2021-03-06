#description Placeholder

import discord, datetime, time
from discord.ext import commands
from bot import start_time, slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='kick', description='Placeholder', guild_ids=[757508676784488559], options=None)
    async def kick(self, ctx: SlashContext):
        pass

def setup(bot):
    bot.add_cog(kick(bot))