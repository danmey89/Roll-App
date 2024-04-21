import random as rd

with open("data.csv", "r") as f:
    d: list = f.readlines()
for index, i in enumerate(d):
    i = i.removesuffix("\n")
    i = [int(v) if v.isnumeric() else v for v in i.split(",")]
    d[index] = i
print(d)


def roll(val):
    for idx, i in enumerate(d[1:]):
        g = rd.randrange(1, 21, 1)
        n = i[val] + g
        if g == 20:
            print("Ergebnis für %s: %d Nat 20!!!" % (d[idx + 1][0], n))
        if g == 1:
            print("Ergebnis für %s: %d Nat 1!!!" % (d[idx + 1][0], n))
        else:
            print("Ergebnis für %s: %d" % (d[idx + 1][0], n))


while True:
    uval = input("Please enter modifier: ")
    if uval in d[0][1:]:
        roll(d[0].index(uval))
    elif uval == "end":
        break
    else:
        print("Modifier not found, please try again.")
