import sys

input = sys.stdin.readline

N = int(input())

result = []
for _ in range(N):
    result.append(int(input()))

print("\n".join(map(str, sorted(result))))
