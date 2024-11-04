import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def status(ctx, member: discord.Member):
    if member.presence is not None:
        await ctx.send(f"{member.name}'s status is {member.presence.status}")
        if member.activity:
            await ctx.send(f"{member.name} is currently {member.activity.name}")
    else:
        await ctx.send(f"Unable to fetch {member.name}'s presence.")

YOUR_BOT_TOKEN = input("Token:")
bot.run(YOUR_BOT_TOKEN)