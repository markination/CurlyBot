import motor.motor_asyncio
import os
async def setup_guild_configuration(guild_id: int):
    """Create a basic guild configuration within the database

    Args:
        guild_id (int): The Guild ID

    Returns:
        bool: True if either a record has been created or a record has been found, False if a record could not be created
    """
    try:
        mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
        db = mongo["Curly"]["Config"]
        find = await db.find_one({"guild_id": guild_id})
        if find:
            return True
        insert = await db.insert_one({"guild_id": guild_id})
        if insert:
            return True
        return False
    except:
        return False

    