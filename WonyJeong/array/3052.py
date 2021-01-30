import sys

input = sys.stdin.readline

arr = []
for _ in range(0, 42):
    arr.append(0)

for i in range(0, 10):
    idx = int(input().strip()) % 42
    arr[idx] += 1

answer = 0

for val in arr:
    if val > 0:
        answer += 1

print(answer)