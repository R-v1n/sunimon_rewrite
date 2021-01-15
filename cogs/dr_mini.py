from discord.ext import commands
import random
import discord
from PIL import Image,ImageDraw


class dragon_game(commands.Cog):

  def __init__(self,bot):
       self.bot=bot

  def hp_calc(self,hp,total):
    val=(hp/total)*19
    r_val=int(val)
    return r_val

  def hp_display(self,hp1,hp2,tot1,tot2):
    #val range between 1 to 19
    val1=self.hp_calc(hp1,tot1)
    val2=self.hp_calc(hp2,tot2)
    if val1==0:
        val1+=1
    val2=self.hp_calc(hp2,tot2)
    if val2==0:
        val2+=1

    x1_org=5
    x1= x1_org + int((val1)-1)*12
    y1=285
    color1=(98,211,245)
    x2_org=362
    y2=293
    x2= x2_org + int((val2)-1)*12
    color2=(235,52,52)
    diam=12
    img=Image.open('/path to file /progress.png').convert('RGB')
    draw=ImageDraw.Draw(img)
    #drawing 1st hp
    draw.ellipse([x1,y1,x1+diam,y1+diam], fill=color1)
    ImageDraw.floodfill(img, xy=(6,291), value=color1, thresh=40)
    text1=f" HP : {hp1}/ {tot1}"
    draw.text((34,286), text1,fill ="black")
    #drawing 2nd hp
    draw.ellipse([x2,y2,x2+diam,y2+diam], fill=color2)
    ImageDraw.floodfill(img, xy=(369,293), value=color2, thresh=40)
    text2=f" HP : {hp2}/ {tot2}"
    draw.text((406,293), text2,fill ="black")
    img.save('/path to file /result.png')

  async def create_embed(self,ctx,nam,hp1,hp2,tot1,tot2):
      cvalue = random.randint(0, 0xffffff)
      embed = discord.Embed(title=f" Dragon Kunj vs {nam} ", description="",color=cvalue)
      #embed.set_thumbnail(url=message.author.avatar_url)
      embed.add_field(name="Dragon Kunj  ", value=f"HP : {hp1} / {tot1} ", inline=True)
      self.hp_display(hp1,hp2,tot1,tot2)
      file= discord.File("/path to file /result.png")
      embed.set_image(url="attachment://result.png")
      embed.add_field(name=f"{nam} ",value=f"HP:{hp2} / {tot2} ", inline=True)
      await ctx.send(file=file,embed=embed)

  def all_move(self,dragon,user):
    flag=1
    x=dragon.attack
    ct=0
    for i in range(1,4):
     y="a"+str(i)
     if x[y]["mov_no"]==0:
          ct+=1
    if ct==3:
       flag=0
       return flag
    x=user.attack
    ct=0
    for i in range(1,4):
     y="a"+str(i)
     if x[y]["mov_no"]==0:
          ct+=1
    if ct==3:
       flag=0
       return flag
    return flag

  def attack_acc(self,x):
     y=random.randint(1,100)
     if y>=x:
        return 0
     else :
        return 1
  async def hp_disp(self,ctx,drhp,ushp,dr_tot,us_tot,uname):
        hp1=drhp
        tot1=dr_tot
        hp2=ushp
        tot2=us_tot
        await self.create_embed(ctx,uname,hp1,hp2,tot1,tot2)
  def mov_check(self,att):
       if att["mov_no"]==0:
          return 0
  class user():
      def __init__(self,x):
          self.name=x
          self.lv=random.randint(1,4)
          self.tot_hp=1200*3+100*self.lv
          self.hp=self.tot_hp
          self.attack= {
                        "a1":{"a_name":"vedi vechu","damage":400,"accuracy":95,"mov_no":20},
                        "a2":{"a_name":"Pst 120 brutal 180 MS ","damage":1000,"accuracy":65,"mov_no":5},
                        "a3":{"a_name":"COvid 20","damage":750,"accuracy":85,"mov_no":10}
                      }
      async def display_attack(self,ctx):
          us_att=self.attack
          m1=us_att["a1"]["mov_no"]
          m2=us_att["a2"]["mov_no"]
          m3=us_att["a3"]["mov_no"]
          """
           att_no          att_name                  damage                   accuracy          no_of_mov
           1>              vedi vechu                400                        95                 {m1}
           2>              Pst 120 brutal 180 MS     1000                       65                 {m2}
           3>              COvid 20                  750                        85                 {m3}
          """
          cvalue = random.randint(0, 0xffffff)
          embed = discord.Embed(title=" Select A move ", description=" enter move.no <1,2,3> or enter /sur to surrender ",color=cvalue)
          embed.add_field(name="att_name : ", value="<< (1) vedi vechu >><< (2) Pst 120 brutal 180 MS >><< (3) COvid 20 >>", inline=False)
          embed.add_field(name="damage : ",value="<< (1) 400 >><< (2) 1000 >><< (3) 750 >>", inline=False)
          embed.add_field(name="accuracy : ",value="<< (1) 95 >><< (2) 65 >><< (3) 85 >>", inline=False)
          embed.add_field(name="no of mov: ",value=f"<< (1) {m1} >><< (2) {m2} >><< (3) {m3} >>", inline=False)
          await ctx.send(embed=embed)
  class dragon():
       def __init__(self):
          self.name="dragon kunju"
          self.lv=random.randint(5,10)
          self.tot_hp=1000*3+100*self.lv
          self.hp=self.tot_hp
          self.attack={
                        "a1": {"a_name":"Thee thuppi","damage":450,"accuracy":90 ,"mov_no":20},
                        "a2":{"a_name":"Flame_disc0","damage":1150,"accuracy":65,"mov_no":5},
                        "a3":{"a_name":"Dragon_dinner","damage":800,"accuracy":85,"mov_no":10}
                      }
 
  async  def battle(self,ctx,user,dragon):
          
          def check(author,channel):
            def check_content(message):
              if message.author!=author or message.channel!=channel:
                return False
              if not(message.content=='1' or message.content=='2' or message.content=='3'):
                return False
              return True
            return check_content

          await ctx.send(f"oh..A {dragon.name} appeared ..")
          await ctx.send("what do u wish to do? ")  
          await ctx.send("1>fight 2>flee 3>fleee ")        
          try:
            msg = await self.bot.wait_for('message',check=check(ctx.author,ctx.channel),timeout=60)
          except Exception as err:
             await ctx.send("invalid input ") 
             return                 
          x=msg.content          
          x=int(x)
          if x==1:             
              flag=0
              init=0
              a_hp=dragon.hp
              b_hp=user.hp
              atot=dragon.tot_hp
              btot=user.tot_hp
              b_name=user.name
              await self.hp_disp(ctx,a_hp,b_hp,atot,btot,b_name)
              y=random.randint(1,2)
              mv=0
              while flag==0:
                  if self.all_move(dragon,user)==0:
                      x="""there is no move left ...
                           ......exiting......"""
                      await ctx.send(x)
                      return
                  if y==1:
                   mv+=1
                   init+=1
                   await ctx.send("select your move ")
                   await user.display_attack(ctx)                   
                   await ctx.send("enter the attack no: ")                  
                   try:
                       msg = await self.bot.wait_for('message',check=check(ctx.author,ctx.channel),timeout=60)
                   except:                   
                       await ctx.send("invalid choice ")
                       await ctx.send("exiting..")
                       return  
                   
                   x=msg.content                                   
                   y="a"+ x

                   att=user.attack[y]
                   while self.mov_check(att)==0:
                     await ctx.send("the number of available move is zero .please select another move..")
                     try:
                       msg = await self.bot.wait_for('message',check=check(ctx.author,ctx.channel),timeout=60)
                     except:                   
                       await ctx.send("invalid choice ")     

                   x=msg.content                     
                   y="a"+ x
                   att=user.attack[y]
                   acc=att["accuracy"]
                   aname=att["a_name"]
                   user.attack[y]["mov_no"]-=1
                   await ctx.send(f"{user.name} used {aname} \n")
                   hit=self.attack_acc(acc)
                   if hit==1:
                       dmg=att["damage"]
                       dragon.hp-=dmg
                   else:
                      await ctx.send("Dragon kunj evaded the attack..")
                   if not dragon.hp<=0:
                     y=2
                   else:
                       flag=1
                       break
                  if mv==2:
                       y=random.randint(1,2)
                  if  init==2:
                   a_hp=dragon.hp
                   b_hp=user.hp
                   b_name=user.name
                   atot=dragon.tot_hp
                   btot=user.tot_hp
                   b_name=user.name
                   await self.hp_disp(ctx,a_hp,b_hp,atot,btot,b_name)
                   init=0

                  if y==2:
                     mv+=1
                     init+=1
                     x=random.randint(1,3)
                     a_nam="a"+str(x)
                     att=dragon.attack[a_nam]
                     while self.mov_check(att)==0:
                       x=random.randint(1,3)
                       a_nam="a"+str(x)
                     acc=att["accuracy"]
                     aname=att["a_name"]
                     dragon.attack[a_nam]["mov_no"]-=1
                     await ctx.send(f" Dragon kunj used {aname} ")
                     hit=self.attack_acc(acc)
                     if hit==1:
                         dmg=att["damage"]
                         user.hp-=dmg
                     else:
                         await ctx.send(f"{user.name} evaded the attack..")
                     if not user.hp<=0:
                       y=2
                     else:
                         flag=1
                         break
                     y=1
                  if mv==2:
                      y=random.randint(1,2)
                      mv=0
                  if  init==2:
                   a_hp=dragon.hp
                   b_hp=user.hp
                   b_name=user.name
                   atot=dragon.tot_hp
                   btot=user.tot_hp
                   b_name=user.name
                   await self.hp_disp(ctx,a_hp,b_hp,atot,btot,b_name)
                   init=0
              if dragon.hp<=0:
                  disp="-"*30+" [ GAME OVER ] "+"-"*30
                  await ctx.send(disp)
                  mess=f"""----------------------------------
                       dragon kunj fainted..
                       {user.name} defeated dragon kunju
                   """
                  await ctx.send(mess)
              elif user.hp<=0:
                 disp="-"*30+" [ GAME OVER ] "+"-"*30
                 await ctx.send(disp)
                 await ctx.send(f"Dragon kunj defeated {user.name}")
          elif x==2 or x==3 or x==4 :
              await ctx.send(f"{user.name} fled...")
              return
  
  @commands.command(name='dr')
  async def drag_mini(self,ctx):
       uname=ctx.author.name
       dr=self.dragon()
       usr=self.user(uname)
       await self.battle(ctx,usr,dr)

def setup(bot):
  bot.add_cog(dragon_game(bot))