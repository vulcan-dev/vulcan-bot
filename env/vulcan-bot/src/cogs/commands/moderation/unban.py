#description Placeholder

import discord, datetime, time
from discord.ext import commands
from bot import start_time, slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

class unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='unban', description='Placeholder', guild_ids=[757508676784488559], options=None)
    async def unban(self, ctx: SlashContext):
        pass

def setup(bot):
    bot.add_cog(unban(bot))