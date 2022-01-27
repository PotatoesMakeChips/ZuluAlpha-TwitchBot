import os
import asyncio
from twitchio.ext import commands

class BotChat(commands.Bot):
    ## setup
    def __init__(self):
        super().__init__(
                        token=os.environ['TOKEN'],
                        client_id=os.environ['CLIENT_ID'],
                        nick=os.environ['BOT_NICK'],
                        prefix=os.environ['BOT_PREFIX'],
                        initial_channels=[os.environ['CHANNEL']]
                        )


    ## events

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')
        channelObj = self.get_channel(os.environ['CHANNEL'])
        loop = asyncio.get_event_loop()
        print(os.environ['CHANNEL'])
        loop.create_task(channelObj.send("/me has arived"))
    async def event_message(self, message):
        'Runs every time a message is sent in chat.'

        # make sure the bot ignores itself and the streamer
        if message.echo:
            return
        message.send("lol")
        await self.handle_commands(message)

if __name__ == "__main__":
    ZuluAlphaPotato = BotChat()
    ZuluAlphaPotato.run()
