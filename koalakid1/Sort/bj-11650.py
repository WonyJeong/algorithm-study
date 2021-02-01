import sys
import operator

input = sys.stdin.readline

N = int(input())

result = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    result.append((x, y))

result = sorted(result, key=operator.itemgetter(0, 1))

for x, y in result:
    print(f"{x} {y}")
