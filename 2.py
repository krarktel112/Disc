import discord

user_id = "450867169581072394"
TOKEN = input("Token:")

async def fetch_user_info(bot, user_id):
    user = await bot.fetch_user(user_id)
    user2 = bot.fetch_user(user_id)
    print(f"User: {user.name}#{user.discriminator}")
    print(f"ID: {user.id}")
    print(f"Bot: {user.bot}")
    attributes = dir(user)
    print(attributes)
    
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    await fetch_user_info(bot, user_id)

bot.run(TOKEN)
