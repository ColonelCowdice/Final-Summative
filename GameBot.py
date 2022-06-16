from discord.ext import commands
import Timer

client = commands.Bot(command_prefix='?')

if Timer == "2048 Loss":
    @client.command
    async def ping(ctx):
        await ctx.send('You suck at 2048')

elif Timer == "Tetris Loss":
    @client.command
    async def ping(ctx):
        await ctx.send('You suck at Tetris')





client.run('My bot token, cant post it on github sorry')