times = input("number? : ")

length = 0
number = 5
temp = number
templen = length
dims = number
ninja = True
while ninja:
    if temp == 1:
        if templen > length:
            length = templen
            dims = number
            number = temp
            temp = number+ 1
    print temp
    if temp % 2 == 0:
        temp = temp/2
        templen += 1
        print temp
    else:
        temp = temp *3 +1
        templen += 1
    print temp
    if temp == times:
        ninja = False
