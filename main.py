# Im Bored, Wise Words:
# An idiot admires complexity, a genius admires simplicity

import dotenv
dotenv.load_dotenv()
import sys
sys.dont_write_bytecode = True
import discord
from discord.ext import commands
import os
import asyncio
import dotenv
from cogwatch import watch
from typing import Literal, Optional
from motor.motor_asyncio import AsyncIOMotorClient
dotenv.load_dotenv()

TOKEN = os.getenv(os.getenv("env"))
intents = discord.Intents.all()


class bot(commands.AutoShardedBot):
    def __init__(self):
        self.mongo = AsyncIOMotorClient(os.getenv("MONGO_URI"))
        super().__init__(command_prefix='!!', intents=intents)

    @watch(path='Cogs', preload=True)
    async def on_ready(self):
        await self.tree.sync()
        print('Bot ready.')
        await self.change_presence(activity=discord.CustomActivity(name=os.getenv("ACTIVITY")))
        
discordbot = bot()

async def run():
    
    for root, dirs, files in os.walk('./Cogs'):
        for filename in files:
            if filename.endswith('.py'):
                relative_path = os.path.relpath(os.path.join(root, filename), './')
                extension_name = os.path.splitext(relative_path)[0].replace(os.sep, '.')
                
        
                    
                try:
                    await discordbot.load_extension(extension_name)
                except:
                    pass
    view = discord.ui.View(timeout=None)               
    
if __name__ == '__main__':
    
    asyncio.run(run())
    discordbot.run(TOKEN)
    