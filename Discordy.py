import discord
import asyncio
import datetime


class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        discord.Client.__init__(self, **kwargs)

    @asyncio.coroutines
    def on_ready(self):
        servers = list(self.servers)
        for server in servers:
            if server.name == 'My server':
                break

        for channel in server.channels:
            if channel.name == 'general':
                break

        now = datetime.datetime.now()
        yield from self.send_message(channel, 'Api Success! at ' + str(now))
        print('Success!')
        yield from self.close()


if __name__ == '__main__':
    dc = DiscordClient()
    email = input('email : ')
    password = input('password : ')
    dc.run(email, password)