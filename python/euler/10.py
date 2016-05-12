def isprime(n):
    for x in xrange(3, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

sum=0;
for i in xrange(1,int(2e6),2):
    if isprime(i):
        sum += i


print sum
