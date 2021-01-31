
import sys

input = sys.stdin.readline

num = int(input())

print(2 ** num - 1)


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    hanoi(n-1, a, c, b)
    print(a, c)
    hanoi(n-1, b, a, c)


hanoi(num, 1, 2, 3)
