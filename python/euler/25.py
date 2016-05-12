def fib(n):
    if n==1 or n ==2:
        return 1

    fibs = [1, 1]
    while len(str(fibs[-1])) < 1000:
        fibs.append(fibs[-2]+fibs[-1])
    return len(fibs)
inpu = input("number: ")
print(fib(inpu))
