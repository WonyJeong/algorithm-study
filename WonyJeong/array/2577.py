import sys

input = sys.stdin.readline

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = 1
for i in range(0, 3):
    result = result * int(input().strip())

for i in range(len(str(result))):
    arr[int(str(result)[i])] += 1

for _ in arr:
    print(_)