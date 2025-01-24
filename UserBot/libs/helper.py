import discord
from discord import SyncWebhook
from datetime import datetime
from. import config

webhook = SyncWebhook.from_url(config.LogWebhook)

def log_command(command_name: str, user: discord.User, message: str, channel: discord.abc.GuildChannel, guild: discord.Guild):  # Send Command Use Log

    embed = discord.Embed(
        title="Command Log",
        description="A command was used.",
        color=0x3498db 
    )
    embed.add_field(name="Command", value=command_name, inline=False)
    embed.add_field(name="User", value=f"{user} (ID: {user.id})", inline=False)
    embed.add_field(name="Message", value=message, inline=False)
    embed.add_field(name="Channel", value=f"{channel} (ID: {channel.id})", inline=False)
    embed.add_field(name="Guild", value=f"{guild} (ID: {guild.id})", inline=False)
    embed.add_field(name="Time", value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.set_footer(text="made by no.1_jj")

    webhook.send(embed=embed, username="Command Logger")
     #Made By no.1_jj
