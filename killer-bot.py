import csv
import random
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get
from random import randint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

knockerDict = {}
miniLedger = {}


#black door questions
with open('blackdoor.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    blackdoor_list = (list(reader))

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

#The Reach
with open('re.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    re_list = (list(reader))      

#put everything in one list (except the world bosses, dungeons, and high profile targets) and shake it up... you know, just for fun.
anything_list = target_list + cw_list + gc_list + hb_list + mm_list + ws_list + ew_list + vv_list + se_list + ss_list + wg_list + re_list
random.shuffle(anything_list)

bot = commands.Bot(command_prefix='$')

def compose_response(random_target):
    # random_target is a dictionary, and the key names like 'CONTRACT_NUMBER'
    # come from the header row in the CSV file. So if your spreadsheet has
    # different headers, change this response string accordingly.
     return f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"

def detect_farmer(player, prefix):
    # we'll detect if someone requested 3 contracts in a row from the
    # same zone. Some of the zones have very few contracts and tend to
    # be farmable. We didn't care much about this before, but now that
    # we have a monthly kill count contest we really need to discourage
    # this behavior pattern. Luckily, I happen to be intimately acquainted
    # with the bot's innards...
    if player in miniLedger:
        if prefix in miniLedger[player]:
           if miniLedger[player][prefix] == 3:
               miniLedger.pop(player)
               return True
           else:
                miniLedger[player][prefix] += 1
                return False
        else:
            miniLedger.pop(player)
            miniLedger[player][prefix] = 1
            return False
    else:
        #the key entry for the player has to be initialized to an empty dict or you get a keyerror.
        miniLedger[player] = {} 
        miniLedger[player][prefix] = 1
        return False

# I think everybody's dice bot uses this logic.
def roll(roll):
    rolling = []
    roll = roll.lower()
    try:
        for x in range(int(roll.split('d')[0])):
            rolling.append(randint(1,int(roll.split('d')[1])))
        return f'You rolled {" ".join(str(x) for x in rolling)}, which has a total of {sum(rolling)}'
    except Exception as err:
        return f'I cannot roll that. I need it in 2d6 format, please.'


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
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(cw_list))) 

@bot.command(name='gc', brief='gets a gold coast random target')
async def goldcoast(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(gc_list))) 

@bot.command(name='hb', brief='gets a hews bane random target')
async def hewsbane(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(hb_list))) 


@bot.command(name='mm', brief='gets a murkmire random target')
async def murkmire(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(mm_list))) 

@bot.command(name='ws', brief='gets a western skyrim random target')
async def skyrim(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(ws_list))) 

@bot.command(name='ew', brief='gets a northern elsweyr random target')
async def elsweyr(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(ew_list))) 

@bot.command(name='vv', brief='gets a vvardenfell random target')
async def vvardenfell(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(vv_list))) 

@bot.command(name='se', brief='gets a southern elsweyr random target')
async def southelsweyr(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(se_list))) 

@bot.command(name='ss', brief='gets a summerset random target')
async def summerset(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(ss_list))) 

@bot.command(name='wg', brief='gets a wrothgar random target')
async def wrothgar(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(wg_list))) 

@bot.command(name='gd', brief='gets a group dungeon random target')
async def dungeon(ctx):
    await ctx.send(compose_response(random.choice(gd_list)))

@bot.command(name='re', brief='gets a reach random target')
async def reach(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(re_list))) 

@bot.command(name='hp', brief='gets a high profile random target')
async def dungeon(ctx):
    isFarmer = detect_farmer(ctx.author.id, ctx.prefix)
    if isFarmer:
        await ctx.send(compose_response(random.choice(target_list)))
    else:
        await ctx.send(compose_response(random.choice(hp_list))) 

@bot.command(name='anything', brief='gets a random target from anywhere (no world bosses)')
async def anything(ctx):
    await ctx.send(compose_response(random.choice(anything_list)))

@bot.command(name='knock', brief='see help knock for details', help='knock on the black door. used when first joining. when you get the question, type $knock [answer] to respond. ex: $knock beans')
async def knock(ctx):
    if ctx.author.id in knockerDict:
        if knockerDict[ctx.author.id]['KEYWORD'].lower() in ctx.message.content.lower():
            await ctx.send('yes, the answer is ' + knockerDict[ctx.author.id]['ANSWER'])
            role = get(ctx.guild.roles, name='Verified Member')
            await ctx.author.add_roles(role)
        else:
            await ctx.send('that is not correct. The question was: ' + knockerDict[ctx.author.id]['QUESTION'])
    else: #add the user n crap to the dict if he didn't exist
        knockerDict[ctx.author.id] = random.choice(blackdoor_list)
        await ctx.send(knockerDict[ctx.author.id]['QUESTION'])

@bot.command(name='dice', brief='rolls xdy dice. ex: $dice 2d4')
async def dice(ctx, arg='1d6'):
    await ctx.send(roll(arg))

bot.run(TOKEN)


