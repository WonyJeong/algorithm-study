import sys

input = sys.stdin.readline

N = int(input())

result = [0] * 10001
for _ in range(N):
    data = int(input())
    result[data] += 1

for i in range(len(result)):
    if result[i] != 0:
        for _ in range(result[i]):
            print(i)
