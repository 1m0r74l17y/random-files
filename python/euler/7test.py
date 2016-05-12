option = input("Prime number?")
def isPrime(option):
    if option % 2 == 0: return False
    p = 3
    while p < option**0.5+1:
        if option % p == 0: return False
        p += 2
    return True

print(isPrime(option))
