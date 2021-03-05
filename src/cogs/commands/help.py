#description Outputs this

import discord
from utils import utils
from os import listdir
from discord.ext import commands
from bot import slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

#ignore this file (maybe)
#prefix + name of file
#for every file in commands, add that as title and read var description
#check if first 2 words are same, if so make them inline (set_chn_log, set_chn_welcome)
#open file, read #description 123

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command()
    @cog_ext.cog_slash(name='Help', description='Lists useful commands', guild_ids=[757508676784488559], options=None)
    async def help(self, ctx: SlashContext):
        embed=discord.Embed(title='Commands', color=0x01dae9)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        prefix = utils.load_settings()['prefix']
        for file in listdir('./cogs/commands/'):
            if file.endswith('.py'):
                desc = open(f'./cogs/commands/{file}', 'r+').readline().replace('#description', '')
                embed.add_field(name=f'{prefix}{file[:-2]}', value=desc)

        await ctx.respond()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))