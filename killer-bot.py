import csv
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

with open('targets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    target_list = (list(reader))

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='contract')
async def contract(ctx):
    random_target= random.choice(target_list)
    # random_target is a dictionary, and they key names like 'CONTRACT_NUMBER'
    # come from the header row in the CSV file. So if your spreadsheet has
    # different headers, change this response string accordingly.
    response = f"Contract # {random_target['CONTRACT_NUMBER']}\nName: {random_target['TARGET']}\nZone: {random_target['ZONE']}\n{random_target['LEDGER_TEXT']}"
    await ctx.send(response)

bot.run(TOKEN)


