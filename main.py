from datetime import datetime
from logging import error
import discord
import os
from discord import guild
from discord import colour
from discord.ext import commands
from discord import client
from discord import embeds
from discord.colour import Color
from discord.embeds import E
from discord.ext import commands, tasks
from discord.ext.commands.help import MinimalHelpCommand
from discord.role import R
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord import user
import time
import random
from youtube_dl import YoutubeDL
from discord.channel import VoiceChannel
import asyncio
import json
from TOKEN import TOKEN

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\VxG")

client = commands.Bot(command_prefix=['vxg.', 'sv.'])

client.remove_command('help')

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='**VxG Help**', description='Use command `vxg.help <all/category/commands>` to view more commands and de', color=ctx.author.color)        
    em.add_field(name='Moderation', value='`kick ban unban\nmute unmute clear\narole rrole crole\ndrole send`')
    em.add_field(name='Action', value='`hello chui ranimg`')
    em.add_field(name='Invite', value='`invite`')
    await ctx.send(embed = em)

@help.command()
async def category(ctx):
    em = discord.Embed(title='**V-Moderation Help**', description='', color=ctx.author.color) 
    em.add_field(name='**Category**', value='Moderation\nAction\nInvite')
    await ctx.send(embed = em)



async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['coins'] = 0
    with open('coins_data.json', 'w') as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open('coins_data.json', 'r') as f:
        users = json.load(f)
    return users


async def update_bank(user, change = 0, mode = 'coins'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('coins_data.json', 'w') as f:
        json.dump(users, f)
    bal = [users[str(user.id)]['coins']] 
    return bal

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
async def load(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
