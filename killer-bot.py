import os
import random
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
from discord_slash import SlashCommand
from dotenv import load_dotenv
import utilities

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_ids = os.environ.get("GUILD_IDS").split(" ")
#discord wants the ids as integers
guild_ids = [int(id) for id in guild_ids]
bot = commands.Bot(command_prefix='$')
# Declares slash commands through the client.
slash = SlashCommand(bot, sync_commands=True) 

#filename variables
targetFile = 'targets.csv'
dlcFiles =['cw.csv','gc.csv','hb.csv','mm.csv','ws.csv','ew.csv',
           'vv.csv','se.csv','ss.csv','wg.csv','re.csv','bw.csv']
wbFile = 'wb.csv'
hpFile = 'hp.csv'

# Declare and fill the lists
target_list = utilities.listFiller(targetFile)
wb_list = utilities.listFiller(wbFile)
hp_list = utilities.listFiller(hpFile)
anything_list = []
anything_list.extend(target_list)
for dlcFile in dlcFiles:
    anything_list.extend(utilities.listFiller(dlcFile))
random.shuffle(anything_list)

#build a dictionary of commands and associate them with target lists
commandDict= {}
commandDict['base'] = target_list
commandDict['wb'] = wb_list
commandDict['hp'] = hp_list
commandDict['anything'] = anything_list

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# /contract gets a base game random target
@slash.slash(name="contract", description=
             'Type /contract help for a list of types.Defaults to base game.',
             guild_ids=guild_ids)
async def contract(ctx, arg='base'):
    if arg in commandDict:
        await ctx.send(utilities.compose_response(
                       random.choice(commandDict[arg]))) 
    else:
        await ctx.send("I can issue the following contract types:\n " + 
                       "/contract base (base game contract)\n " + 
                       "/contract wb (world bosses)\n" + 
                       "/contract hp (high profile, see a speaker)\n" + 
                       "/contract anything (base game plus all DLC)")  

@slash.slash(name='dice', description='rolls xdy dice. ex: /dice 2d4', 
             guild_ids=guild_ids)
async def dice(ctx, arg='1d6'):
    await ctx.send(utilities.roll(arg))

if __name__ == "__main__":
    bot.run(TOKEN)


