import random as rd
import math

arr = list()
n = 10000

for i in range(0, n):
    arr.append(rd.randrange(1, 21, 1))

print(arr)


def tausche(p, a, b):
    p[a], p[b] = p[b], p[a]


def sort(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i+1, l):
            if arr[j] < arr[min]:
                min = j
        tausche(arr, min, i)


sort(arr)
print(arr)

c = 0
count = [0] * arr[-1]


for i in range(len(arr)):
    if arr[i] == c + 1:
        count[c - 1] += 1
        c = arr[i]
    elif arr[i] == arr[i-1]:
        count[c - 1] += 1
    else:
        c = arr[i]

m = sum(count) / len(count)
k = float()

for i in count:
    j = float(i) - m
    k += (j * j)
s = math.sqrt(k / len(count))

print(count)
print(sum(count))
print(len(arr))
print(sum(arr) / len(arr))
print(m)
print(s)


