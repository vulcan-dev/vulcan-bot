import discord, datetime, time
from discord.ext import commands
from bot import start_time, slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext

class uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='Uptime', description='Displays the bot\'s uptime', guild_ids=[757508676784488559], options=None)
    async def uptime(self, ctx: SlashContext):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(title=f'{self.bot.user.name}\'s Uptime', colour=0x01dae9)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name="Uptime", value=text)
        try:
            await ctx.respond()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            pass

        #await ctx.message.delete()

def setup(bot):
    bot.add_cog(uptime(bot))