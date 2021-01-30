import sys

input = sys.stdin.readline

num = int(input())

for i in range(1, num+1):
    n, m = map(int, input().strip().split())
    print(f"Case #{i}: {n+m}")
