import discord
from discord import client
from discord import embeds
from discord.ext import commands
import random
import time
from discord.ext.commands import Bot, has_permissions, CheckFailure

class sendmes():
    @commands.command()
    @has_permissions(kick_members=True)
    async def send(self, ctx, channel: discord.TextChannel, em=None, *, message):
            if em=='embed':
                em = discord.Embed(title='', description=f'{message}', colour=discord.Colour(0xff9d00)) 
                await channel.send(embed = em)
            else:
                await channel.send(message)
    


        

    @send.error
    async def send_message_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)
    

