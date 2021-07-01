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

# Declare and fill the lists
target_list = utilities.listFiller('targets.csv')
cw_list = utilities.listFiller('cw.csv')
gc_list = utilities.listFiller('gc.csv')
hb_list = utilities.listFiller('hb.csv')
mm_list = utilities.listFiller('mm.csv')
ws_list = utilities.listFiller('ws.csv')
ew_list = utilities.listFiller('ew.csv')
vv_list = utilities.listFiller('vv.csv')
se_list = utilities.listFiller('se.csv')
ss_list = utilities.listFiller('ss.csv')
wg_list = utilities.listFiller('wg.csv')
re_list = utilities.listFiller('re.csv')
bw_list = utilities.listFiller('bw.csv')
wb_list = utilities.listFiller('wb.csv')
hp_list = utilities.listFiller('hp.csv')
anything_list = target_list + cw_list + gc_list + hb_list + mm_list \
                + ws_list + ew_list + vv_list + se_list + ss_list \
                + wg_list + re_list + bw_list
random.shuffle(anything_list)
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


