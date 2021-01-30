import sys

input = sys.stdin.readline

a, b, c = map(int, input().strip().split())

profit = c - b

if profit <= 0:
    print(-1)
else:
    print(a//profit + 1)
