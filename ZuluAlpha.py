import os
import asyncio
from twitchio.ext import commands
import Rules
import AlertLogger

class BotChat(commands.Bot):
    ## setup
    def __init__(self):
        super().__init__(
                        token=os.environ['TOKEN'],
                        client_id=os.environ['CLIENT_ID'],
                        nick=os.environ['BOT_NICK'],
                        prefix=os.environ['BOT_PREFIX'],
                        initial_channels=os.environ['CHANNELS'].split(',')
                        )


    ## events

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')
    async def event_message(self, message):
        'Runs every time a message is sent in chat.'

        # make sure the bot ignores itself and the streamer
        if message.echo:
            return
        Rules.checkMessage(message.author.name,message.content)
        ## handles commands from message events
        await self.handle_commands(message)
    ## commands

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx: commands.Context):
        if ctx.author.is_mod:
            await ctx.send(f'Hello {ctx.author.name}!')
            AlertLogger.logAlert(str(ctx.author.name),"System Test","<test command>")


if __name__ == "__main__":
    ZuluAlpha = BotChat()
    ZuluAlpha.run()
