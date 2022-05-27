import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands import Bot, has_permissions, CheckFailure
import time
import random
import json
import os

class shop():
    @commands.command()
    async def shop(self, ctx):
        em = discord.Embed(title='**VxG Shop**', description='''Use **vxg.info <item id>** to get more details about an item.
        Use **vxg.buy <item id>** to buy an item.
        ''')
        await ctx.send(embed=em)