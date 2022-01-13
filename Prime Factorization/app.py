def isPrime(x):
    for i in range(2,(x//2) + 1):
        if x % i == 0 and x != i:
            return False

    return True

def nextPrime(x):
    for i in range(2, (x // 2) + 1):
        if (x % i == 0 and isPrime(i) == True):
            return i
    return x

def primeFactorize(x):

    arr = []

    while x != 1:
        prime = nextPrime(x)
        arr.append(prime)
        x //= prime

    return arr

arr = primeFactorize(3782)
arr.reverse()
print(arr)