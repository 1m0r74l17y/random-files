
import time,sys
while True:
    blah = "********"
    for l in range(10):
        sys.stdout.write("*")
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.2)
