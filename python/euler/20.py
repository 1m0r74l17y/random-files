import math

def fuck(me):
    stuff = 1
    for i in range(me):
        stuff *= (i+1)
    return stuff

def sumfuck(trees):
    sum = 0
    for number in range(len(str(trees))):
        add = str(trees)
        sum += int(add[number])
    return sum
test = input("number")
print sumfuck(fuck(test))
