import discord

user_id = "450867169581072394"
TOKEN = input("Token:")

async def fetch_user_info(bot, user_id):
    user = await bot.fetch_user(user_id)
    print(f"User: {user.name}#{user.discriminator}")
    print(f"ID: {user.id}")
    print(f"Bot: {user.bot}")
    print(user_status)
async def user_status(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
        status = user.status
        await ctx.send(f"The user's status is: {status}")
    except discord.NotFound:
        await ctx.send("User not found.")
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    await fetch_user_info(bot, user_id)


bot.run(TOKEN)
