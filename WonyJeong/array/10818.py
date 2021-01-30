import sys

input = sys.stdin.readline

max = -1000001
min = 1000001

N = int(input().strip())
arr = list(map(int, input().strip().split()))

for val in arr:
    if val > max:
        max = val
    if val < min:
        min = val

print(f"{min} {max}")
