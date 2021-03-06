#description Displays information for the server
#may have copied and pasted this code from https://github.com/Carberra/updated-discord.py-tutorial/blob/master/lib/cogs/info.py
#I've been coding all day alright? leave me alone. ps, really nice code. apologies for stealing it but I have excuses

from discord import Embed, Member
from discord.ext import commands
from bot import slash
from datetime import datetime
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from typing import Optional

class server_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='serverinfo', description='Outputs user info', guild_ids=[757508676784488559], options=None)
    async def server_info(self, ctx: SlashContext):
        embed = Embed(title="Server information",
                        colour=ctx.guild.owner.colour,
                        timestamp=datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("ID", ctx.guild.id, True),
                    ("Owner", ctx.guild.owner, True),
                    ("Region", f'{str(ctx.guild.region).title()}', True),
                    ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                    ("Members", len(ctx.guild.members), True),
                    ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                    ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                    ("Banned members", len(await ctx.guild.bans()), True),
                    ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
                    ("Text channels", len(ctx.guild.text_channels), True),
                    ("Voice channels", len(ctx.guild.voice_channels), True),
                    ("Categories", len(ctx.guild.categories), True),
                    ("Roles", len(ctx.guild.roles), True),
                    ("Invites", len(await ctx.guild.invites()), True),
                    ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.respond()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(server_info(bot))