from math import sqrt

def LHS(n):
    sum = 0
    for k in range(1,n+1):
        sum += sqrt((k-1)*(4/n)) * (4/n)
    return sum

def RHS(n):
    sum = 0
    for k in range(1, n + 1):
        sum += (1/(1+(k/n))) * (1/n)
    return sum

def MID(n):
    sum = 0
    for k in range(1, n + 1):
        sum += (1/(1+(k-0.5)*(1/n)))*(1/n)
    return sum

print(LHS(50))


