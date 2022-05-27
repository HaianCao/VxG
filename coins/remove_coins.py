import discord
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands import Bot, has_permissions, CheckFailure
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


async def update_bank(user, change = 0, mode = 'coins'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('coins_data.json', 'w') as f:
        json.dump(users, f)
    bal = [users[str(user.id)]['coins']] 
    return bal

class remove_coins():
    @commands.command()
    @has_permissions(administrator=True)
    async def removecoins(self, ctx, member:discord.Member, *, coin: str):
        await open_account(member)
        users = await get_bank_data()
        bal = await update_bank(member)
        coin = str(coin)
        def convert_str_to_number(x): #x truyền vào phải là string
            total_stars = 0
            num_map = {'k':1000, 'K':1000, 'm':1000000, 'M':1000000, 'b':1000000000, 'B':1000000000}
            if x.isdigit():
                total_stars = int(x)
            else:
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(coin)
        users[str(member.id)]['coins'] -= amount
        with open('coins_data.json', 'w') as f:
            json.dump(users, f)
        await ctx.send('Removed successful!')

    @removecoins.error
    async def drole_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)

    @commands.command()
    @has_permissions(administrator=True)
    async def removecoin(self, ctx, member:discord.Member, *, coin: str):
        await open_account(member)
        users = await get_bank_data()
        bal = await update_bank(member)
        coin = str(coin)
        def convert_str_to_number(x): #x truyền vào phải là string
            total_stars = 0
            num_map = {'k':1000, 'K':1000, 'm':1000000, 'M':1000000, 'b':1000000000, 'B':1000000000}
            if x.isdigit():
                total_stars = int(x)
            else:
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(coin)
        users[str(member.id)]['coins'] -= amount
        with open('coins_data.json', 'w') as f:
            json.dump(users, f)
        await ctx.send('Removed successful!')

    @removecoin.error
    async def drole_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            em = discord.Embed(title='', description='Bạn không có quyền sử dụng command này', color=ctx.author.color) 
            await ctx.send(embed = em)