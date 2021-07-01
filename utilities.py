import csv
from random import randint

def listFiller(fileName):
    with open (fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        return (list(reader))
     
def compose_response(random_target):
    # random_target is a dictionary, and the key names like
    # 'CONTRACT_NUMBER' come from the header row in the CSV 
    # file. So if your spreadsheet has different headers, 
    # change this response string accordingly.
     return (f"Contract # {random_target['CONTRACT_NUMBER']}\n" +
            f"Name: {random_target['TARGET']}\n" +
            f"Zone: {random_target['ZONE']}\n" +
            f"{random_target['LEDGER_TEXT']}")

# I think everybody's dice bot uses this logic.
def roll(roll):
    rolling = []
    roll = roll.lower()
    try:
        for x in range(int(roll.split('d')[0])):
            rolling.append(randint(1,int(roll.split('d')[1])))
        return (f'You rolled {" ".join(str(x) for x in rolling)},' +
                f'which has a total of {sum(rolling)}')
    except Exception as err:
        return f'The argument provided was not in XdY format. ex: 2d6'
