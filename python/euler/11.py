import math
count = []
number = 1
numbers = []
while len(count) <= 5 :
    add = "no"
    count = []

    for i in range(number):
        if number % (i+1) == 0:
            count.append(i+1)
            # print len(count)
            # print count
            if add == "no":
                numbers.append(number)
                add = "yes"
    number += 1


print numbers
