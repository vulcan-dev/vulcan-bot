#description Displays information of x user
#may have copied and pasted this code from https://github.com/Carberra/updated-discord.py-tutorial/blob/master/lib/cogs/info.py
#I've been coding all day alright? leave me alone. ps, really nice code. apologies for stealing it but I have excuses

from discord import Embed, Member
from discord.ext import commands
from bot import slash
from datetime import datetime
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from typing import Optional

options = [
    {
        'name': 'target',
        'description': 'target to get info from',
        'required': True,
        'type': 6
    }
]

class user_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='userinfo', description='Outputs user info', guild_ids=[757508676784488559], options=options)
    async def user_info(self, ctx: SlashContext, target: Optional[Member]):
        target = target or ctx.author

        embed = Embed(
            title='User Information',
            colour=target.colour,
            timestamp=datetime.utcnow()
        )

        fields = [
            ('ID', target.id, False),
            ('Name', str(target), True),
            ('Bot?', target.bot, True),
            ('Top Role', target.top_role.mention, True),
            ('Status', str(target.status).title(), True),
            ('Activity', f'{str(target.activity)}', False),
            ('Created at', target.created_at.strftime('%d/%m/%Y %H:%M:%S'), True),
            ('Joined at', target.joined_at.strftime('%d/%m/%Y %H:%M:%S'), True),
            ('Boosted', bool(target.premium_since), False)
        ]

        embed.set_thumbnail(url=target.avatar_url)

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.respond()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(user_info(bot))