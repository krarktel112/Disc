import discord
import asyncio
import datetime


class DiscordClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self, intents=discord.Intents.default())
    print('Success!')
    yield from self.close()


if __name__ == '__main__':
    dc = DiscordClient()
    email = input('email : ')
    password = input('password : ')
    dc.run(email, password)
