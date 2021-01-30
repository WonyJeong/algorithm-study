import sys

input = sys.stdin.readline


def getScore(answer):
    result = 0
    idx = 0

    for i in range(len(answer)):
        if answer[i] == "O":
            idx += 1
            if i == len(answer) - 1:
                result += int((idx * (idx + 1)) / 2)
        else:
            result += int((idx * (idx + 1)) / 2)
            idx = 0

    print(result)


N = int(input().strip())
for _ in range(0, N):
    getScore(input().strip())
