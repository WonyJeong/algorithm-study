import sys
import math


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


def factorization(num):
    if isPrime(num) == 1:
        print(num)
        return 1
    root = math.ceil(math.sqrt(num))
    for i in range(2, root+1):
        if isPrime(i) == 1:
            while True:
                if num % i == 0:
                    print(i)
                    num //= i
                else:
                    break
        if num == 1:
            break
    return num


input = sys.stdin.readline
num = int(input())

while True:
    num = factorization(num)
    if num == 1:
        break
