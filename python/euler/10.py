def isprime(n):
    for x in xrange(3, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

sum=0;
num = input("what number? : ")
for i in xrange(1,num,2):
    if isprime(i):
        sum += i


print sum + 1
