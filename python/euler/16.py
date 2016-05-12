import math
number = 2
def twopower(me):
    stuff = 2
    for i in range(me-1):
        stuff *= number
    return stuff

def sumfuck(trees):
    sum = 0
    for number in range(len(str(trees))):
        add = str(trees)
        sum += int(add[number])
    return sum
test = input("number")
print sumfuck(twopower(test))
