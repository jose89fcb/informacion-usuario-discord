import discord
from discord.ext import commands,tasks
import datetime 
from itertools import cycle
from colorama import Fore, init
from datetime import datetime
import pytz # $ pip install pytz

init()


intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '!', intents=intents)





import locale

locale.setlocale(locale.LC_ALL, 'es-ES') 
@bot.command()

async def usuarioinfo(ctx, *, member:discord.Member =None):
 
    if member == None:
            member = ctx.message.author
            
    
    
    nick = (str(member.nick).replace("None","Ninguna"))
    status_dict = {
      "online" : "En linea! 🟢",
      "offline": "Desconectado! ⚪", 
      "idle"   : "Ausente! 🟡",
      "dnd"    : "No molestar! 🔴",
      "invisible"  : "Invisible ⚪"
    }
    status = status_dict[str(member.status)]
    
    botman_dict = {
    "False": "No",
    "True":  "Sí"
    }
    botman = botman_dict[str(member.bot)]

    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    
        
    embed=discord.Embed(title="Información usuario", description="\n\n**Nombre:** " + f"{member.name}" "\n\n**Apodo:** " f"{nick}" + "\n\n**ID: **" + f"{member.id}" + "\n\n**Bot?: **" + f"{botman}" + "\n\n**Cuenta Creada:** "+ member.created_at.strftime("%A %d %B %Y %I:%M") + "\n\n**Se ha unido:** " + member.joined_at.strftime("%A %d %B %Y %I:%M") + "\n\n**Posición:** "+ str(members.index(member)+1) + "\n\n**Estado:** " + f"{status}",  timestamp=datetime.utcnow(),colour=discord.Colour.random())

    embed.set_thumbnail(url=member.avatar_url)
   

    await ctx.send(embed=embed)
      


     
       
    
   
             

        


       
        
            


@bot.event
async def on_ready():
    print("BOT listo! registro chat")

 
 
 
bot.run('')    #Crea un bot e un Token: https://discord.com/developers/applications
