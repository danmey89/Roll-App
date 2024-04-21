from csv import DictReader
from functions import roll

with open("data.csv", "r") as f:
    dict_reader = DictReader(f)
    data = list(dict_reader)

for index, i in enumerate(data):
    i = dict((k, int(v)) if v.isnumeric() else (k, v) for k, v in i.items())
    data[index] = i


while True:
    uval = input("Please enter modifier: ")
    if uval in data[0].keys():
        for player in data:
            print(roll(uval, player))
    elif uval == "end":
        break
    else:
        print("Unknown input , please try again!")
