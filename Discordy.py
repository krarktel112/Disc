import asyncio
import datetime


# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

x = input("Token:")
client.run('MTI0Mjk1NDU5MTY4ODIwMDI4Mg.Gxk_yG.Pq3HX4fHayQmf7mj1bZfHzeRGta8Dh1XWBYCXY')
