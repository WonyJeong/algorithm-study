import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

print((m-45 < 0 and n == 0) and "23" or m-45 < 0 and f'{n-1}' or n, end=" ")
print(m-45 < 0 and m + 60 - 45 or m - 45)
