import discord
from discord.ext import commands
from youtube.announcement import sendmes

class youtube(commands.Cog, sendmes):
    def __init__(self, client):
        self.client = client
        self.send = sendmes


def setup(client):
    client.add_cog(youtube(client))