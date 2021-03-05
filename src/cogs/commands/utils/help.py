#description Outputs all commands in an embed

import discord
from utils import utils
from os import listdir
from discord.ext import commands
from bot import slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

import os
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='Help', description='Lists useful commands', guild_ids=[757508676784488559], options=None)
    async def help(self, ctx: SlashContext):
        embed=discord.Embed(title='Commands', color=0x01dae9)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        prefix = utils.load_settings()['prefix']
        for path, subdirs, files in os.walk('./cogs/commands/'):
            for file in files:
                if file.endswith('.py'):
                    desc = open(f'{path}/{file}', 'r+').readline()
                    if (desc.split()[0] == '#description'):
                        embed.add_field(name=f'{prefix}{file[:-2]}', value=desc.replace('#description', ''))
                    else: embed.add_field(name=f'{prefix}{file[:-2]}', value='N/A')

        await ctx.respond()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))