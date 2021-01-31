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


N, M = map(int, input().strip().split())

for i in range(N, M+1):
    if isPrime(i) == 1:
        print(i)
