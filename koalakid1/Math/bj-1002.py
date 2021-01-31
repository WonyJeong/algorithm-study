import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    r = ((x2-x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)
    print(-1 if r == 0 and r1 == r2 else 1 if r ==
          r1 + r2 or m == sum(R) else 0 if m > sum(R) else 2)
