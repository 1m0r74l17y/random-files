import math

a = input("a : ")
b = input("b : ")
c = input("c : ")

d = b*b-(4*a*c)


print



print str("d : ") + str(d)

if d == 0.0 or 0:
    sqrtd = math.sqrt(d)
    x = -b/(2*a)
    print "x : " + str(x)

if d < 0:
    print "there is no x."

if d > 0:
    sqrtd = math.sqrt(d)
    x1 = (-b+sqrtd)/(2*a)
    print "x+ : " + str(x1)
    x2 = (-b-sqrtd)/(2*a)
    print "x- : " + str(x2)
