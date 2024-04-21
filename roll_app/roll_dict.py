from csv import DictReader
import random

with open("data.csv", "r") as f:
    dict_reader = DictReader(f)
    data = list(dict_reader)

for index, i in enumerate(data):
    i = dict((k, int(v)) if v.isnumeric() else (k, v) for k, v in i.items())
    data[index] = i


def roll(l_val):
    for player in data:
        g = random.randrange(1, 21, 1)
        m = g + player[l_val]
        if g == 20:
            print("Ergebnis für %s: %d Nat 20!!!" % (player["name"].capitalize(), m))
        if g == 1:
            print("Ergebnis für %s: %d Nat 1!!!" % (player["name"].capitalize(), m))
        else:
            print("Ergebnis für %s: %d" % (player["name"].capitalize(), m))


while True:
    uval = input("Please enter modifier: ")
    if uval in data[0].keys():
        roll(uval)
    elif uval == "end":
        break
    else:
        print("Unknown input , please try again!")
