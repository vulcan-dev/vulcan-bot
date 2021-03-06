#description Placeholder

import discord, datetime, time
from discord.ext import commands
from bot import start_time, slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='ban', description='Placeholder', guild_ids=[757508676784488559], options=None)
    async def ban(self, ctx: SlashContext):
        pass

def setup(bot):
    bot.add_cog(ban(bot))