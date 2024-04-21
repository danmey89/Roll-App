import random


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