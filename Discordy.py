import discord
import asyncio
import datetime

client = discord.Client()

@client.event()
async def on_ready():
    print("Bot is online")

client.login()
