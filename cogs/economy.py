import discord
import discord
from discord.ext import commands
from coins.balance import balance
from coins.add_coins import add_coins
from coins.remove_coins import remove_coins


class economy(commands.Cog, balance, add_coins, remove_coins):
    def __init__(self, client):
        self.client = client
        self.coins = balance 
        self.addcoins = add_coins
        self.removecoins = remove_coins

def setup(client):
    client.add_cog(economy(client))