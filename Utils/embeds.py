import json, discord

def recursively_replace(obj, key, value):
    if isinstance(obj, str):
        return obj.replace(key, value)
    elif isinstance(obj, list):
        return [recursively_replace(item, key, value) for item in obj]
    elif isinstance(obj, dict):
        return {k: recursively_replace(v, key, value) for k, v in obj.items()}
    else:
        return obj
    
def clean_input(input_value):
    """
    Strips whitespace from the input value and returns None if it's empty.
    """
    stripped_value = input_value.strip() if input_value else ""
    return None if not stripped_value else stripped_value
