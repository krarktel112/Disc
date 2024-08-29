import discord
client = discord.Client(intents=discord.Intents.default())
client.event
async def on_ready():
print("the bot is now online")
client.event
async def on_message(message):
if message.content == 'example':
await message.content.send("example reply the bot is supposed to make")
client.run("this is just the discord ticket which functions normally")

