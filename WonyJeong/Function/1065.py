import sys

input = sys.stdin.readline


def hansu(_n):
    if _n < 100:
        return 1
    n = str(_n)
    if int(n[2]) - int(n[1]) == int(n[1]) - int(n[0]):
        return 1
    return 0


N = input().strip()

answer = 0
for i in range(1, int(N) + 1):
    answer += hansu(i)
print(answer)