from discord.ext import commands
import discord
class suni_pic(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def sunipic(self,ctx):
        await ctx.send(file=discord.File("{file_path}/files/sunimon.png"))

def setup(bot):
    bot.add_cog(suni_pic(bot))
    

