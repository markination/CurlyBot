import motor.motor_asyncio
import os
from Utils.modules import get_guild_configuration

async def get_module_configuration(guild_id: int, module_name: str):
    """Gets the guild configuration for the module defined in module_name

    Args:
        guild_id (int): The Guild ID
        module_name (str): The name of the module and the object in the record

    Returns:
        list
    """
    try:
        mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
        db = mongo["Curly"]["Config"]
        find = await get_guild_configuration(guild_id)
        if isinstance(find, bool):
            return False
        if find:
            data = find[module_name]
            if data:
                return data

    except:
        return False

async def create_module_configuration(guild_id: int, module_name: str):
    """Creates the guild configuration for the module defined in module_name

    Args:
        guild_id (int): The Guild ID
        module_name (str): The name of the module and the object in the record

    Returns:
        bool
    """
    try:
        mongo = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
        db = mongo["Curly"]["Config"]
        find = await get_guild_configuration(guild_id)
        if isinstance(find, bool):
            return False
        await db.update_one(find, {"$set": {f"{module_name}": {}}})
        return True

    except:
        return False

    