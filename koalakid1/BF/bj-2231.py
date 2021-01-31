import sys

input = sys.stdin.readline

N = int(input())

result = 0
for i in range(1, N):
    sumVal = i
    for j in str(i):
        sumVal += int(j)
    if sumVal == N:
        result = i
        break
print(result)
