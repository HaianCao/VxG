import discord
from discord.ext import commands
from discord.ext.commands.core import command
import time
import random
import json
import os

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\VxG")

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

class balance():
    @commands.command()
    async def coins(self, ctx, *, member:discord.Member = None):
        if member==None:
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()
            coins_amt = users[str(user.id)]['coins']
            em = discord.Embed(description=f'{ctx.author.mention} has **{coins_amt}VG** :partying_face:', colour=ctx.author.color)
            await ctx.send(embed=em)
        if member != None:
            users = await get_bank_data()
            if str(member.id) not in users:
                await ctx.send('The specified user does not have a balance')
                return
            coins_amt = users[str(member.id)]['coins']
            em = discord.Embed(description=f'{member.mention} has **{coins_amt}VG** :partying_face:', colour=member.color)
            await ctx.send(embed=em)

    @commands.command()
    async def coin(self, ctx, *, member:discord.Member = None):
        if member==None:
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()
            coins_amt = users[str(user.id)]['coins']
            em = discord.Embed(description=f'{ctx.author.mention} has **{coins_amt}VG** :partying_face:', colour=ctx.author.color)
            await ctx.send(embed=em)
        if member != None:
            users = await get_bank_data()
            if str(member.id) not in users:
                await ctx.send('The specified user does not have a balance')
                return
            coins_amt = users[str(member.id)]['coins']
            em = discord.Embed(description=f'{member.mention} has **{coins_amt}VG** :partying_face:', colour=member.color)
            await ctx.send(embed=em)