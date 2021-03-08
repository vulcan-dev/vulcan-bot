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
    # Moderation
    'cogs.commands.moderation.ban',
    'cogs.commands.moderation.kick',
    'cogs.commands.moderation.unban',
    'cogs.commands.moderation.warn',

    # Utils
    'cogs.commands.utils.bdel',
    'cogs.commands.utils.git',
    'cogs.commands.utils.set_chn_log',
    'cogs.commands.utils.set_chn_welcome',
    'cogs.commands.utils.set_chn_rules',
    'cogs.commands.utils.help',
    'cogs.commands.utils.uptime',
    'cogs.commands.utils.user_info',
    'cogs.commands.utils.server_info',

    # Events
    'cogs.events.on_message',
    'cogs.events.on_message_edit',
    'cogs.events.on_message_delete',
    'cogs.events.on_voice_state_update',
    'cogs.events.reaction_roles',
]

@bot.event
async def on_ready():
    utils.logger.info(f'Logged in as {bot.user.name}')
    try:
        await bot.change_presence(activity=discord.Game(name="Daniel W is a shit owner"))
    except errors.HTTPException as e:
        utils.logger.error(f'HTTPException: {str(e)}')

    await message.add_reaction('✅')

try:
    for ext in extensions:
        bot.load_extension(ext)
        utils.logger.info(f'Loaded extension: {ext}')

    utils.logger.info(f'Finished loading extenions')
    bot.run(utils.get_token())
except Exception as e:
    print(f'ERROR: {e}')
    utils.logger.warning(e)