import sys

input = sys.stdin.readline

x = int(input())
y = int(input())

print((x > 0 and y > 0) and 1 or (x < 0 and y > 0)
      and 2 or (x < 0 and y < 0) and 3 or 4)
