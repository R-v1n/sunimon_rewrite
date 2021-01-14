from discord.ext import commands
import random
class c_flip(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        
    @commands.command()
    async def cflip(self,ctx):
        def check(author,channel):
            def check_content(message):            
                if message.author!=author or message.channel!=channel:
                  return False
                if not (message.content=="heads" or message.content=="tails"):
                  return False
                return True
            return check_content    
        await ctx.send("heads or tails")
        msg=await self.bot.wait_for('message',check=check(ctx.author,ctx.channel),timeout=30)
        nam=ctx.author
        y=random.randint(1,2)
        if y==1:
           outc="heads"
        elif y==2:
           outc="tails"
        x=msg.content   
        if x == outc :
          await ctx.send(f'eda mw0nee {nam} ... {x} aada')
        elif x!=outc :          
          await ctx.send(f'sorry eda mw0nee {nam} ...{outc} aanu..better luck next time.')
          
def setup(bot):
    bot.add_cog(c_flip(bot))