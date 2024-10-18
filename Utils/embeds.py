import json, discord

def convert_embed(embed_data, replacements):
    try:
        
        for key, value in replacements.items():
            embed_data = recursively_replace(embed_data, key, value)
        
        embed_list = []
        for embed_data_item in embed_data.get("embeds", []):
            if isinstance(embed_data_item, dict):
                embed = discord.Embed.from_dict(embed_data_item)
                embed_list.append(embed)
            else:
                print("Invalid embed data format:", embed_data_item)
        
        return embed_list
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []

def recursively_replace(obj, key, value):
    if isinstance(obj, str):
        return obj.replace(key, value)
    elif isinstance(obj, list):
        return [recursively_replace(item, key, value) for item in obj]
    elif isinstance(obj, dict):
        return {k: recursively_replace(v, key, value) for k, v in obj.items()}
    else:
        return obj
    