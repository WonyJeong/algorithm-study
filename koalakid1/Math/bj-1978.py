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
item = list(map(int, input().strip().split()))
count = 0
for i in item:
    count += isPrime(i)
print(count)
