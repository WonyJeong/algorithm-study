import sys

input = sys.stdin.readline

n = int(input())

print(n >= 90 and "A" or n >= 80 and "B" or n >=
      70 and "C" or n >= 60 and "D" or "F")
