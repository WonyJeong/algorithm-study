import sys

input = sys.stdin.readline

N = int(input().strip())
num = input().strip()

answer = 0

for i in range(0, N):
    answer += int(num[i])

print(answer)