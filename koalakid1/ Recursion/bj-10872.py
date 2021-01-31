
import sys

input = sys.stdin.readline

num = int(input())


def factorial(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2
    return num * factorial(num-1)


print(factorial(num))
