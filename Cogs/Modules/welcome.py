import discord
from discord.ext import commands
import os
import motor
import motor.motor_asyncio

class WelcomeCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.mongo_uri = os.getenv("MONGO_URI")
    
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if os.getenv("ENVIORMENT").lower() != "production":
            return
        if member.bot:
            return
        mongo = motor.motor_asyncio.AsyncIOMotorClient(self.mongo_uri)
        collection = mongo["Curly"]["Config"]
        find = await collection.find_one({"guild_id": member.guild.id})
        if not find:
            return
        
        

        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(WelcomeCog(client))
    
