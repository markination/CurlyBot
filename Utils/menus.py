import discord
import json
import typing
from discord import InteractionResponse, Webhook
from Utils.emojis import Emojis

async def interaction_check_failure(responder: typing.Union[InteractionResponse, Webhook, typing.Callable]):
    if isinstance(responder, typing.Callable):
        responder = responder()

    if isinstance(responder, InteractionResponse):
        await responder.send_message(content=f"{Emojis.no_emoji} You can't use these buttons.", ephemeral=True)
    else:
        await responder.send(content=f"{Emojis.no_emoji} You can't use these buttons.", ephemeral=True)

class CustomModal(discord.ui.Modal, title="Placeholder"):
    def __init__(self, title, options):
        super().__init__(title=title)
        self.saved_items = {}
        for name, option in options:
            self.add_item(option)
            self.saved_items[name] = option

    async def on_submit(self, interaction: discord.Interaction):
        for key, item in self.saved_items.items():
            setattr(self, key, item.value)  
        await interaction.response.defer()

class YesNoMenu(discord.ui.View):
    def __init__(self, user_id: str = None):
        super().__init__(timeout=60000.0)
        self.value = None
        self.user_id = user_id
        self.interaction = None

    async def common_button_action(self, interaction: discord.Interaction, value: bool):
        await interaction.response.defer()
        for item in self.children:
            item.disabled = True
        self.value = value
        self.interaction = interaction
        await interaction.edit_original_response(view=self)
        self.stop()

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.user_id:
            return await self.common_button_action(interaction, True)
        else:
            print(self.user_id)
            print(interaction.user.id)
            await interaction.response.defer(ephemeral=True, thinking=True)
            await interaction_check_failure(interaction.followup)

    @discord.ui.button(label="No", style=discord.ButtonStyle.danger)
    async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.user_id:
            return await self.common_button_action(interaction, False)
        else:
            print(self.user_id)
            print(interaction.user.id)
            await interaction.response.defer(ephemeral=True, thinking=True)
            await interaction_check_failure(interaction.followup)