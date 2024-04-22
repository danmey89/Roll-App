import random
from csv import DictReader
import json


# basic dice roll output  changes needed
def roll(l_val, player):
    g = random.randrange(1, 21, 1)
    m = g + player[l_val]

    if g == 20:
        result = ("Ergebnis für %s: %d Nat 20!!!" % (player["name"].capitalize(), m))
        return result

    elif g == 1:
        result = ("Ergebnis für %s: %d Nat 1!!!" % (player["name"].capitalize(), m))
        return result

    else:
        result = ("Ergebnis für %s: %d" % (player["name"].capitalize(), m))
        return result


# load character data from csv  to be replaced
FILEPATH = "data1.csv"


def get_data(filepath=FILEPATH):
    with open(filepath, "r") as f:
        dict_reader = DictReader(f)
        data = list(dict_reader)

    for index, i in enumerate(data):
        i = dict((k, int(v)) if v.isnumeric() else (k, v) for k, v in i.items())
        data[index] = i
    return data


# turn order add turn
def get_order(numb, name, order_l):
    numb = int(numb)
    new = numb, name
    order_l.append(new)
    order_l = sorted(order_l, key=lambda pair: pair[0], reverse=True)
    return order_l


# json file reader
def get_json(filepath):
    with open(filepath) as f:
        file = f.read()
        file = json.loads(file)
        return file


# Pathbuilder json to dict converter
def get_character(file):
    trs = file
    print(type(trs))
    trs = trs["build"]
    modifier_dict = get_json("test_data\\modifier_keyes.json")

    abilities = {'str': trs["abilities"]['str'], 'dex': trs["abilities"]['dex'],
                 'con': trs["abilities"]['con'], 'int': trs["abilities"]['int'],
                 'wis': trs["abilities"]['wis'], 'cha': trs["abilities"]['cha']}

    abilities = dict((k, [v, ""]) for k, v in abilities.items())

    for abi in abilities:
        c = abilities[abi][0]
        m = modifier_dict[str(c)]
        abilities[abi][1] = m

    proficiencies = {'perception': [trs["proficiencies"]['perception'], "wis", ""],
                     'fortitude save': [trs["proficiencies"]['fortitude'], "con", ""],
                     'reflex save': [trs["proficiencies"]['reflex'], "dex", ""],
                     'will save': [trs["proficiencies"]['will'], "wis", ""],
                     'acrobatics': [trs["proficiencies"]['acrobatics'], "dex", ""],
                     'arcana': [trs["proficiencies"]['arcana'], "int", ""],
                     'athletics': [trs["proficiencies"]['athletics'], "str", ""],
                     'crafting': [trs["proficiencies"]['crafting'], "int", ""],
                     'deception': [trs["proficiencies"]['deception'], "cha", ""],
                     'diplomacy': [trs["proficiencies"]['diplomacy'], "cha", ""],
                     'intimidation': [trs["proficiencies"]['intimidation'], "cha", ""],
                     'medicine': [trs["proficiencies"]['medicine'], "wis", ""],
                     'nature': [trs["proficiencies"]['nature'], "wis", ""],
                     'occultism': [trs["proficiencies"]['occultism'], "int", ""],
                     'performance': [trs["proficiencies"]['performance'], "cha", ""],
                     'religion': [trs["proficiencies"]['religion'], "wis", ""],
                     'society': [trs["proficiencies"]['society'], "int", ""],
                     'stealth': [trs["proficiencies"]['stealth'], "dex", ""],
                     'survival': [trs["proficiencies"]['survival'], "wis", ""],
                     'thievery': [trs["proficiencies"]['thievery'], "dex", ""]}

    for key in proficiencies:
        if proficiencies[key][0] == 2:
            proficiencies[key][2] = "trained"
        elif proficiencies[key][0] == 4:
            proficiencies[key][2] = "expert"
        elif proficiencies[key][0] == 6:
            proficiencies[key][2] = "master"
        elif proficiencies[key][0] == 8:
            proficiencies[key][2] = "legend"
        else:
            proficiencies[key][2] = "untrained"

    for key in proficiencies:
        if proficiencies[key][2] in ("trained", "expert", "master", "legend"):
            proficiencies[key][0] += trs["level"]

    for key in proficiencies:
        proficiencies[key][0] += abilities[proficiencies[key][1]][1]

    char = {'name': trs["name"], 'class': trs["class"], 'level': trs["level"],
            "abilities": abilities, "proficiencies": proficiencies}

    return char
