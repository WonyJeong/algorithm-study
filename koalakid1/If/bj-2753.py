import sys

input = sys.stdin.readline

n = int(input())

print(((n % 4 == 0 and n % 100 != 0) or n % 400 == 0) and 1 or 0)
