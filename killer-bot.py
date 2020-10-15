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
with open('clockwork.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    clockwork_list = (list(reader))

#gold coast contracts
with open('goldcoast.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    goldcoast_list = (list(reader))

#hew's bane contracts
with open('hewsbane.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    hewsbane_list = (list(reader))

#murkmire contracts
with open('murkmire.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    murkmire_list = (list(reader))

#western skyrim contracts
with open('skyrim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    skyrim_list = (list(reader))

#put everything in one list (except the world bosses) and shake it up... you know, just for fun.
anything_list = target_list + clockwork_list + goldcoast_list + hewsbane_list + murkmire_list + skyrim_list
random.shuffle(anything_list)

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# !contract gets a base game random target
@bot.command(name='contract', brief='gets a base game contract')
async def contract(ctx):
    random_target= random.choice(target_list)
    # random_target is a dictionary, and they key names like 'CONTRACT_NUMBER'
    # come from the header row in the CSV file. So if your spreadsheet has
    # different headers, change this response string accordingly.
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !wb gets a base game random world boss
@bot.command(name='wb',brief='gets a base game random world boss')
async def wb(ctx):
    random_target= random.choice(wb_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !cw gets a clockwork city random target
@bot.command(name='cw', brief='gets a clockwork city random target')
async def clockwork(ctx):
    random_target= random.choice(clockwork_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !gc gets a gold coast random target
@bot.command(name='gc', brief='gets a gold coast random target')
async def goldcoast(ctx):
    random_target= random.choice(goldcoast_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !hb gets a hew's bane random target
@bot.command(name='hb', brief='gets a hews bane random target')
async def hewsbane(ctx):
    random_target= random.choice(hewsbane_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !mm gets a murkmire random target
@bot.command(name='mm', brief='gets a murkmire random target')
async def murkmire(ctx):
    random_target= random.choice(murkmire_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !ws gets a western skyrim random target
@bot.command(name='ws', brief='gets a western skyrim random target')
async def skyrim(ctx):
    random_target= random.choice(skyrim_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

# !anything gets a random target from the jumbled up list (minus world bosses)
@bot.command(name='anything', brief='gets a random target from anywhere (no world bosses)')
async def anything(ctx):
    random_target= random.choice(anything_list)
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

bot.run(TOKEN)


