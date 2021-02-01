import sys
import operator

input = sys.stdin.readline

N = int(input())

result = {i: [] for i in range(1, 51)}
for _ in range(N):
    string = input().strip()
    length = len(string)
    if string not in result[length]:
        result[length].append(string)

for key, value in result.items():
    if value != []:
        for item in sorted(value):
            print(item)
