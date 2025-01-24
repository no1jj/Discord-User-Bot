import discord
from discord.ext import commands
from discord import app_commands
from discord import SyncWebhook
from datetime import datetime
from enum import Enum
from libs import *

class EmbedColors(Enum):
    Red = discord.Colour.red()
    Orange = discord.Colour.orange()
    Yellow = discord.Colour.yellow()
    Green = discord.Colour.green()
    Blue = discord.Colour.blue()

class MyClient(discord.Client):

    async def on_ready(self):
        print(f"Made by no.1_jj")
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="send", description="message a send") # Send A Message
async def SendMessage(interaction: discord.Interaction, message: str):
    user = interaction.user
    channel = interaction.channel
    guild = interaction.guild
    await interaction.response.send_message(f'{message}', ephemeral=True)
    await interaction.followup.send(f'{message}')
    helper.log_command(command_name="/send", user=user, message=message, channel=channel, guild=guild) # Send Log Message

@client.tree.command(name="mass", description="mass message(maximum number is 5)") # Send Mess Message
async def MassMessage(interaction: discord.Interaction, message: str, count: int = None):
    user = interaction.user
    channel = interaction.channel
    guild = interaction.guild
    if count is None:
        count = 5
    elif count > 5:
        await interaction.response.send_message(f"The maximum number is 5.\nThe {count} you entered is too many.", ephemeral=True)
        return  
    else:
        count = int(count)

    await interaction.response.send_message(f"Sending {count} messages...", ephemeral=True)

    for _ in range(count):
        await interaction.followup.send(f'{message}')
        helper.log_command(command_name="/mass", user=user, message=message, channel=channel, guild=guild) # Send Log Message


@client.tree.command(name="embed", description="embed message") # Send Embed message
async def EmbedMessage(interaction: discord.Interaction, title: str, description: str, footer: str=None, color: EmbedColors=None): #색깔 정하는거랑 footer 정하는거 오류있음
    user = interaction.user
    channel = interaction.channel
    guild = interaction.guild

    if color is None:
        color = discord.Colour.default()

    embed = discord.Embed(title=title, description=description, color=color)
    await interaction.response.send_message(embed=embed, ephemeral=True)
    await interaction.followup.send(embed=embed)
    embed.set_footer(text=footer)

    helper.log_command(command_name="/embed", user=user, message=f"Title: {title} Description: {description}", channel=channel, guild=guild)  # Send Log Message

client.run(config.Token) # Bot Run
 #Made By no.1_jj
