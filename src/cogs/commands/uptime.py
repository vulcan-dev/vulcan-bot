import discord, datetime, time
from discord.ext import commands
from bot import start_time

class uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        try:
            await ctx.channel.send(embed=embed)
        except discord.HTTPException:
            await ctx.channel.send("Current uptime: " + text)

        await ctx.message.delete()

def setup(bot):
    bot.add_cog(uptime(bot))