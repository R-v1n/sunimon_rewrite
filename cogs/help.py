from discord.ext import commands
import discord
import random
class help_cmd(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def help(self,ctx):
        cvalue = random.randint(0, 0xffffff)
        embed = discord.Embed(title=" HELP ", description=" hello nyan Sun1_m0n.Available commands are :",color=cvalue)
        embed.add_field(name="!sunipic",value="send sun1_m0n pic", inline=False)
        embed.add_field(name="!cflip",value="coin flip", inline=False)
        embed.add_field(name="!candb",value="play cows and bulls", inline=False)
        embed.add_field(name="!dr",value="Dragon Kunj mini game", inline=False)
        embed.add_field(name="!yts {search term }",value="search yt vid", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()    
    async def on_ready(self):
         print(f'Logged in as ::>> {self.bot.user.name} ')

    @commands.Cog.listener()    

    async def on_member_join(self,member):       
        channel=member.guild.system_channel
        await channel.send("welcome {member}..Nyan sunim0n")


def setup(bot):
    bot.add_cog(help_cmd(bot))

