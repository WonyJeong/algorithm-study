import sys

input = sys.stdin.readline

count = 0
maxCount = 0
maxVal = 0
for _ in range(9):
    count += 1
    n = int(input())
    if n == max(maxVal, n):
        maxCount = count
        maxVal = n

print(maxVal)
print(maxCount)
