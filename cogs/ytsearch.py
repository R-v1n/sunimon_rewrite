from discord.ext import commands
import discord
import urllib.parse,urllib.request,re
class ytseach(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def yts(self,ctx,arg1,arg2):
        keyword=arg1        
        nor=int(arg2) 
        if nor>5:
            nor=5
        query = urllib.parse.urlencode({'search_query':keyword})        
        url= urllib.request.urlopen('http://www.youtube.com/results?' + query)       
        search_results = re.findall(r'/watch\?v=(.{11})',url.read().decode())        
        if nor==1:
            await ctx.send('http://www.youtube.com/watch?v=' + search_results[1])
            return
        for i in range(int(nor)):
            url_keys='http://www.youtube.com/watch?v=' + search_results[i]            
            await ctx.send(url_keys)       
    @yts.error
    async def usage(self,ctx,error):
        await ctx.send("usage : !yts    keyword      no_of_results(max:5)")
        await ctx.send(f"[error]: {error}")
def setup(bot):
    bot.add_cog(ytseach(bot))        