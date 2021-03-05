import discord
from discord.ext import commands
from discord import errors, CategoryChannel
from utils import utils
from collections import OrderedDict

class on_voice_state_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild = self.bot.get_guild(757508676784488559)
        self.gid = 0

#member - name
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            if after.channel != None:
                self.guild = self.bot.get_guild(member.guild.id)
                if after.channel.id == 817474742332162049:
                    member_role = discord.utils.get(self.guild.roles, name="Member")
                    overwrites = {
                        self.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                        member_role: discord.PermissionOverwrite(view_channel=True)
                    }

                    # Create Category and store it in a variable (vccat) - voice chat category
                    new_category = await self.guild.create_category(name="ᵁˢᵉʳ ⱽᶜ'ˢ", position=2, overwrites=overwrites)
                    vccat = discord.utils.get(self.guild.categories, id=new_category.id)

                    # Create new voice channel
                    new_channel = await self.guild.create_voice_channel(name=f'{member.display_name}\'s ᶜʰᵃⁿⁿᵉˡ', category=vccat)
                    print(new_channel.id)

                    # Set permission for new channel
                    # Move member to that new channel
                    await new_channel.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                    await member.move_to(new_channel)

                    # Check if the new_channel is empty and also check if there's any channels in the new category
                    def check(x, y, z):
                        return len(new_channel.members) == 0 or new_category.channels == 0

                    await self.bot.wait_for('voice_state_update', check=check)
                    await new_channel.delete()
                    print('channel deleted')
                    channels.remove(f'{new_channel}')
                    await new_category.delete()
                    print('category deleted')
        except Exception as e:
            raise e
    
def setup(bot):
    bot.add_cog(on_voice_state_update(bot))