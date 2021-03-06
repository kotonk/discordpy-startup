from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


    
    
@bot.command("zh-caution")
async def tips(ctx):
    await ctx.send('請小心您的隊伍、符文、魂魔吧！')
    
    
bot.run(token)
