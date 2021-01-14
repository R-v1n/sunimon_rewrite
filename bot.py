import discord
from discord.ext import commands
bot=commands.Bot(command_prefix="!",help_command=None)
bot.load_extension("cogs.help")
bot.load_extension("cogs.suni_pic")
bot.load_extension("cogs.cflip")
bot.load_extension("cogs.candb")
#bot.load_extension("cogs.dr_mini")
bot.load_extension("cogs.ytsearch")
token="enter your token here "
bot.run(token)
