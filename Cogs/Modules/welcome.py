import discord
from discord.ext import commands
import os

class WelcomeCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.mongo_uri = os.getenv("MONGO_URI")
    
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if os.getenv("ENVIORMENT").lower() != "production":
            return
        mongo = self.mongo
        
        
        

        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(WelcomeCog(client))
    
