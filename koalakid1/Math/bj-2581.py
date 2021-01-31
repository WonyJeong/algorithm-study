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


N = int(input())
M = int(input())

count = 0
val = 0
minVal = 0

for i in range(N, M+1):
    prime = isPrime(i)

    if prime == 1:
        val += i
    count += prime
    if prime == 1 and count == 1:
        minVal = i

print(minVal == 0 and -1 or f"{val}\n{minVal}")
