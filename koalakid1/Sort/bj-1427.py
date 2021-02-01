import sys

input = sys.stdin.readline

N = list(input().strip())
print("".join(sorted(N, reverse=True)))
