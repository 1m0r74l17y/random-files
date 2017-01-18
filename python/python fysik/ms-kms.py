print "Convert from m/s to km/t or reversed"
print "[1] m/s to km/t"
print "[2] km/t to m/s"

choice = input("Make a pick : ")



if choice == 1 or 2:
    if choice ==  1:
        m = input("meters : ")
        s = input("seconds : ")
        print "{}km/t".format((m/s)*3.6)
    if choice ==  2:
        km = input("kilometers : ")
        t = input("hours : ")
        print "{}m/s".format((km/t)/3.6)

if choice == 24:
    print "     __       .__  .__         ________    _____  "
    print "    |__| ____ |  | |  |   ____ \_____  \  /  |  | "
    print "    |  |/  _ \|  | |  | _/ __ \ /  ____/ /   |  |_"
    print "    |  (  <_> )  |_|  |_\  ___//       \/    ^   /"
    print "/\__|  |\____/|____/____/\___  >_______ \____   | "
    print "\______|                     \/        \/    |__| "
