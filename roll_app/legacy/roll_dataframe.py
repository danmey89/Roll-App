import pandas as pd
import random

df1 = pd.read_excel("data.xlsx")
u_val = input("Please enter value: ")


def roll(l_val):
    j = 0
    for i in df1[l_val]:
        g = random.randrange(1, 21, 1)
        i += g
        if g == 20:
            print("Ergebnis für %s: %d Nat 20!!!" % (df1.iat[j, 0], i))
        if g == 1:
            print("Ergebnis für %s: %d Nat 1!!!" % (df1.iat[j, 0], i))
        else:
            print("Ergebnis für %s: %d" % (df1.iat[j, 0], i))
        j += 1


while u_val != "end":
    roll(u_val)
    u_val = input("Please enter value: ")
