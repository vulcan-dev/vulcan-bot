import discord
from discord import guild
from discord.ext import commands
from discord import errors
from discord.utils import get
from utils import utils

# Sends, deletes, tries to send again, error is caught so it doesn't continue
class reaction_roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.role_message_id = utils.load_settings()['rules_id']

    #async def remove_reaction()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reactionpayload):
        if not reactionpayload.guild_id:
            return  # Private message
        channelID = utils.load_settings()['chn_rules']
        channel = self.bot.get_channel(int(channelID))
        if channel is None:
            print('Ticket System: Channel not Found!')
        else:
            if reactionpayload.message_id == channel.last_message_id:
                if self.bot.get_user(reactionpayload.user_id):
                    guild = self.bot.get_guild(reactionpayload.guild_id)
                    member = await guild.fetch_member(reactionpayload.user_id)
                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        guild.me: discord.PermissionOverwrite(read_messages=True),
                        member: discord.PermissionOverwrite(read_messages=True)
                    }
                    role = discord.utils.get(guild.roles, name="Member", id=758349936584032287)
                    await member.add_roles(role)
            else:
                pass
    
def setup(bot):
    bot.add_cog(reaction_roles(bot))