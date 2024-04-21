import random
from csv import DictReader


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


FILEPATH = "data1.csv"


def get_data(filepath=FILEPATH):
    with open(filepath, "r") as f:
        dict_reader = DictReader(f)
        data = list(dict_reader)

    for index, i in enumerate(data):
        i = dict((k, int(v)) if v.isnumeric() else (k, v) for k, v in i.items())
        data[index] = i
    return data


def get_order(numb, name, order_l):
    numb = int(numb)
    new = numb, name
    order_l.append(new)
    order_l = sorted(order_l, key=lambda pair: pair[0], reverse=True)
    return order_l
