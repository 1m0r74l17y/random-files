import math
f = open('results of 2grads.txt','w')
a = input("a : ")
b = input("b : ")
c = input("c : ")
f.write("a : {} \n".format(a))
f.write("b : {}\n".format(b))
f.write("c : {}\n".format(c))
d = b*b-(4*a*c)
f.write("\nd : {}\n".format(d))
print
d = b*b-(4*a*c)
print str("d : ") + str(d)

if d == 0.0 or 0:
    sqrtd = math.sqrt(d)
    x = -b/(2*a)
    print "x : " + str(x)
    f.write("x : {}".format(x))
    f.write("d = ({}*{})-(4*{}*{})\n\n".format(b,b,a,c))

if d < 0:
    print "there is no x."
    f.write("there is no x.\n")

    f.write("d = ({}*{})-(4*{}*{})\n\n".format(b,b,a,c))

if d > 0:
    sqrtd = math.sqrt(d)
    x1 = (-b+sqrtd)/(2*a)
    print "x1 : " + str(x1)
    x2 = (-b-sqrtd)/(2*a)
    print "x2 : " + str(x2)
    f.write("x{} : {}".format("1", x1))
    f.write("\n")
    f.write("x{} : {}".format("2", x2))
    f.write("d = ({}*{})-(4*{}*{})\n\n".format(b,b,a,c))

toppunktx = ((-b)/(2*a))
toppunkty = ((-d)/(4*a))

print "T({},{})".format(toppunktx,toppunkty)
f.write("T({},{})".format(toppunktx,toppunkty))
