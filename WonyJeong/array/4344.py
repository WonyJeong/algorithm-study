import sys

input = sys.stdin.readline


def getAverge(data):
    avg = sum(data[1:]) / data[0]

    answer = 0
    for i in range(1, data[0] + 1):
        if avg < data[i]:
            answer += 1
    print(f"{answer / data[0] * 100 :.3f}%")


N = int(input().strip())

for _ in range(0, N):
    getAverge(list(map(int, input().strip().split())))
