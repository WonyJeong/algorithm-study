import sys

input = sys.stdin.readline

x, y, w, h = list(map(int, input().strip().split()))

x_w = abs(x-w)
y_h = abs(y-h)

print(min(x, y, x_w, y_h))
