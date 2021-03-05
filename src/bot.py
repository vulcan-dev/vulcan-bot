from enum import auto
import logging
import discord

from discord_slash.context import SlashContext
from utils import utils
from discord import errors
import time
from discord.ext import commands
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext

bot = commands.Bot(command_prefix=utils.load_settings()['prefix'], intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')

slash = SlashCommand(bot, sync_commands=True)

start_time = time.time()

extensions = [
    'cogs.commands.help',
    'cogs.commands.bdel',
    'cogs.commands.uptime',
    'cogs.commands.set_chn_log',
    'cogs.commands.set_chn_welcome',
    'cogs.commands.set_chn_rules',
    'cogs.events.on_message',
    'cogs.events.on_message_edit',
    'cogs.events.on_message_delete',
    'cogs.events.reaction_roles',
]

@bot.event
async def on_ready():
    utils.logger.info(f'Logged in as {bot.user.name}')
    try:
        await bot.change_presence(activity=discord.Game(name="Daniel W is a shit owner"))
        channel = await bot.fetch_channel(int(utils.load_settings()['chn_rules']))
        await channel.purge(limit=2)

        embed = discord.Embed(title='', description='', color=0xbb00ff)
        embed.set_author(name='Rules', icon_url=bot.user.avatar_url)
        embed.add_field(name='**Rule 1)**', value='Be respectful to all Members, treat them as your friend.', inline=False)
        embed.add_field(name='**Rule 2)**', value=f'Obviously no memes in {bot.get_channel(757508676784488561).mention}', inline=False)
        embed.add_field(name='**Rule 3)**', value='Be a cunt', inline=False)
        embed.set_footer(text=utils.get_time())

        message = await channel.send(embed=embed)
        utils.modify_settings('rules_id', message.id)
    except errors.HTTPException as e:
        utils.logger.error(f'HTTPException: {str(e)}')

    await message.add_reaction('✅')

try:
    for ext in extensions:
        bot.load_extension(ext)
        utils.logger.info(f'Loaded extension: {ext}')

    utils.logger.info(f'Finished loading extenions')
    bot.run(utils.load_settings()['token'])
except Exception as e:
    utils.logger.warning(e)