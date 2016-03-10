import math



n = input("Grundmaengden: ")
r = input("Delmaengden: ")

choice = raw_input("raekkefoelge ligeyldig? y/n : ")
if choice == str("y"):
    print math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
else:
    print math.factorial(n)/math.factorial(n-r)
