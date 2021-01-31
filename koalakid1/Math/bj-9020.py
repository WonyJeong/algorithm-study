import sys
import math

input = sys.stdin.readline


def isPrime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    root = math.ceil(math.sqrt(n))
    for i in range(2, root+1):
        if n % i == 0:
            return 0
    return 1


N = 10000
Primes = [False for _ in range(N+1)]
Primes[2] = True
for i in range(3, N+1, 2):
    if isPrime(i) == 1:
        Primes[i] = True

T = int(input())

for _ in range(T):
    n = int(input())

    for i in range(n//2, 1, -1):
        if Primes[i]:
            if Primes[n-i]:
                print(f"{i} {n-i}")
                break
