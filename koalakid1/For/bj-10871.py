import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
k = []
for i in range(len(l)):
    if l[i] < m:
        k.append(l[i])
print(" ".join(str(i) for i in k))
