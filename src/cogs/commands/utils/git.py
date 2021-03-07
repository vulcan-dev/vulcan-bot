#description Sends an embed of information about the git repo

from discord import Embed
from utils import utils
from os import listdir
from discord.ext import commands
from bot import slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

from github3 import GitHub

class git(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='git', description='Sends an embed with information about this bot', guild_ids=[757508676784488559], options=None)
    async def git(self, ctx: SlashContext):
        gh = GitHub()
        repo = gh.repository('vulcan-dev', 'vulcan-bot')

        embed = Embed(title='Git', color=0x01dae9)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name='Git URL', value=repo.git_url, inline=False)
        embed.add_field(name='Created At', value=repo.created_at, inline=False)
        embed.add_field(name='Last Update', value=repo.updated_at, inline=True)
        embed.add_field(name='Stars', value=repo.stargazers_count, inline=True)
        embed.add_field(name='Size', value=repo.size, inline=True)

        await ctx.respond()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(git(bot))