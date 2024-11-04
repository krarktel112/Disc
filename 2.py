import discord

user_id = "450867169581072394"
TOKEN = input("Token:")

async def fetch_user_info(bot, user_id):
    user = await bot.fetch_user(user_id)
    print(f"User: {user.name}#{user.discriminator}")
    print(f"ID: {user.id}")
    print(f"Bot: {user.bot}")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    await fetch_user_info(bot, user_id)  # Replace with actual user ID
async def on_member_update(self, before, after):
    if before.id == user_id:
        if before.status != discord.Status.online and after.status == discord.Status.online:
            self.send_notification(f'{after.name} has come online!')
            print(f'{after.name} is now Online! Press Enter to exit')
            input()  # Wait for user to press Enter
            await self.close()  # Close the bot


bot.run(TOKEN)
