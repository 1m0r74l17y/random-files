import math,random,time,sys
roll = random.randint(1,6)

for i in range(2):
    blah = "\|/-\|/-"
    for l in blah:
        sys.stdout.write(l)
        roll = random.randint(1,6)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.2)
print "\n\n/*********\ "
if roll == 1:
    print "*         *"
    print "*    @    *"
    print "*         *"
if roll == 2:
    print "*  @      *"
    print "*         *"
    print "*      @  *"
if roll == 3:
    print "*  @      *"
    print "*    @    *"
    print "*      @  *"
if roll == 4:
    print "*  @   @  *"
    print "*         *"
    print "*  @   @  *"
if roll == 5:
    print "*  @   @  *"
    print "*    @    *"
    print "*  @   @  *"
if roll == 6:
    print "*  @   @  *"
    print "*  @   @  *"
    print "*  @   @  *"

print "\*********/\n\n"
