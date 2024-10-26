from main import bot
from discord.ext import commands

class Cog(commands.Cog): 
    def __init__(self, bot: bot):
        self.bot = bot