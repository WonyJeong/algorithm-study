import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    n, m = map(int, input().strip().split())
    print(n+m)
