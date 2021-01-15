from discord.ext import commands
import random
class cows_and_bulls(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    def assign_no(self):
       flag=1
       y=str(random.randint(1,9))
       num=y
       for i in range(3):
          while flag==1:
            x=str(random.randint(1,9))
            y=num
            if x in y:
               flag=1
            else :
               flag=0
          num=num+x
          flag=1
          snum=num
       return snum


    def check_no(self,num):
        flag=0
        if len(num)==4:
          for i in range(4):
              for j in range(4):
                if i!=j:
                   if num[i]==num[j]:
                    flag=1
        
          for i in range(4):
            if num[i]=='0':
                flag=1
        else:
            flag=2
        return flag  

    def c_and_b(self,num1,num2):
        b=0
        c=0
        for i in range(4):
            for j in range(4):
                if i==j:
                    if num1[i]==num2[j]:
                        b+=1
                elif i!=j:
                    if num1[i]==num2[j]:
                        c+=1
        rnum=[]
        rnum.append(b)
        rnum.append(c)
        return rnum


       

    @commands.command(name="candb")
    async def candb_main(self,ctx):               
        num1=self.assign_no()        
        author=ctx.author
        channel=ctx.channel
        def check(author,channel):
            def check_content(message):            
                if message.author!=author or message.channel!=channel:
                  return False
                else:
                  return True
            return check_content                
        await ctx.send('please enter the number of tries .maximum:6')
        msg = await self.bot.wait_for('message',check=check(author,channel),timeout=60)
        x=msg.content
        if not int(x) or int(x)>6:
            await ctx.send("usage : enter a number less than 6 ")
            return  
        for i in range(int(msg.content)):
                await ctx.send('enter a non 0 and non repeating 4 dgit number (timeout : 90 sec).. command /sur to surrender')
                y="/sur"
                surrender=0
                msg = await self.bot.wait_for('message',check=check(author,channel),timeout=90)
                if not msg.content.lower().startswith(y):
                    num2=msg.content
                    flag=1
                    while flag==1:
                       if num2.isdigit():
                           x= self.check_no(num2)
                       else :
                            x==2
                       if x==0:
                           flag=0
                       elif x==1:
                          res="you entered a repeating number  or a number with 0..poyi valla vazhayum nadu \n enter a 4 digit number or /sur to surrender"
                       elif x==2:
                          res="you didn't enter 4 digit number ..neeyokee jeevichittu karyam onnum illa.. \n enter a 4 digit number or /sur to surrender"
                       if flag==1:
                        await channel.send(res)
                        msg = await self.bot.wait_for('message',check=check(author,channel),timeout=60)
                        if not msg.content.lower().startswith(y):
                            num2=msg.content
                        else :
                            flag=0
                            surrender=1
                    if surrender==0:
                      cb=self.c_and_b(num1,num2)
                      bull=cb[0]
                      cow=cb[1]
                      if bull==4:
                           await ctx.send(f"mwonee nee jayichh..ithuthanneyanu number  {num1}")
                           return
                      await ctx.send(f"its {bull} b and {cow} c")
                    else :
                        await ctx.send("thoottu pinmari alle..seD  :-( ")
                        return
        else:
         await ctx.send("thoottu pinmari alle..V3rY_s3D. ;{ ")
         return
        await ctx.send(f"s0rry.. {ctx.author.name}  ...Nee thottu. ente number  {num1}")
        return 

def setup(bot):
    bot.add_cog(cows_and_bulls(bot))        