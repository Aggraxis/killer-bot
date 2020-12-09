import csv
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#base game contracts
with open('targets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    target_list = (list(reader))

#base game world bosses
with open('wb.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    wb_list = (list(reader))

#clockwork city contracts
with open('cw.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    cw_list = (list(reader))

#gold coast contracts
with open('gc.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    gc_list = (list(reader))

#hew's bane contracts
with open('hb.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    hb_list = (list(reader))

#murkmire contracts
with open('mm.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    mm_list = (list(reader))

#western skyrim contracts
with open('ws.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ws_list = (list(reader))

#dungeons
with open('gd.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    gd_list = (list(reader))    

#Northern elsweyr
with open('ew.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ew_list = (list(reader))   

#Vvardenfell
with open('vv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    vv_list = (list(reader))

#Southern Elsweyr
with open('se.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    se_list = (list(reader))

#Summerset
with open('ss.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ss_list = (list(reader))      

#Wrothgar
with open('wg.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    wg_list = (list(reader))  

#High Profile
with open('hp.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    hp_list = (list(reader))  

#put everything in one list (except the world bosses, dungeons, and high profile targets) and shake it up... you know, just for fun.
anything_list = target_list + cw_list + gc_list + hb_list + mm_list + ws_list + ew_list + vv_list + se_list + ss_list + wg_list
random.shuffle(anything_list)

bot = commands.Bot(command_prefix='$')

def compose_response(random_target):
    # random_target is a dictionary, and the key names like 'CONTRACT_NUMBER'
    # come from the header row in the CSV file. So if your spreadsheet has
    # different headers, change this response string accordingly.
     return f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# !contract gets a base game random target
@bot.command(name='contract', brief='gets a base game contract')
async def contract(ctx):
    await ctx.send(compose_response(random.choice(target_list))) 

@bot.command(name='wb',brief='gets a base game random world boss')
async def wb(ctx):
    await ctx.send(compose_response(random.choice(wb_list))) 

@bot.command(name='cw', brief='gets a clockwork city random target')
async def clockwork(ctx):
    await ctx.send(compose_response(random.choice(cw_list))) 

@bot.command(name='gc', brief='gets a gold coast random target')
async def goldcoast(ctx):
    await ctx.send(compose_response(random.choice(gc_list))) 

@bot.command(name='hb', brief='gets a hews bane random target')
async def hewsbane(ctx):
    await ctx.send(compose_response(random.choice(hb_list))) 

@bot.command(name='mm', brief='gets a murkmire random target')
async def murkmire(ctx):
    await ctx.send(compose_response(random.choice(mm_list))) 

@bot.command(name='ws', brief='gets a western skyrim random target')
async def skyrim(ctx):
    await ctx.send(compose_response(random.choice(ws_list))) 

@bot.command(name='ew', brief='gets a northern elsweyr random target')
async def elsweyr(ctx):
    await ctx.send(compose_response(random.choice(ew_list))) 

@bot.command(name='vv', brief='gets a vvardenfell random target')
async def vvardenfell(ctx):
    await ctx.send(compose_response(random.choice(vv_list))) 

@bot.command(name='se', brief='gets a southern elsweyr random target')
async def southelsweyr(ctx):
    await ctx.send(compose_response(random.choice(se_list))) 

@bot.command(name='ss', brief='gets a summerset random target')
async def summerset(ctx):
    await ctx.send(compose_response(random.choice(ss_list))) 

@bot.command(name='wg', brief='gets a wrothgar random target')
async def dungeon(ctx):
    await ctx.send(compose_response(random.choice(wg_list)))

@bot.command(name='gd', brief='gets a group dungeon random target')
async def dungeon(ctx):
    await ctx.send(compose_response(random.choice(gd_list)))

@bot.command(name='hp', brief='gets a high profile random target')
async def dungeon(ctx):
    await ctx.send(compose_response(random.choice(hp_list)))

@bot.command(name='anything', brief='gets a random target from anywhere (no world bosses)')
async def anything(ctx):
    await ctx.send(compose_response(random.choice(anything_list)))

bot.run(TOKEN)


