import sys
import operator

input = sys.stdin.readline

n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

for _ in range(m):
    index = a.index(max(a))
    x = a[index]
    a[index] = 0
    print(index+1)
    if x % 7 == 0:
        a = a[::-1]
