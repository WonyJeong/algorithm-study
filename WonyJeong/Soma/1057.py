import sys

input = sys.stdin.readline


def tournament(N, x, y):
    arr = [0 for _ in range(N)]
    arr[x - 1] = 1
    arr[y - 1] = 1

    len_ = N
    round = 0
    while len_ > 0:
        round += 1
        if len_ % 2 != 0:
            arr.append(0)
            len_ += 1
        nextRound = []
        for i in range(0, len_ - 1, 2):
            temp = arr[i] + arr[i + 1]
            if temp == 2:
                print(round)
                exit(0)
            nextRound.append(temp)

        len_ = len_ // 2
        arr = nextRound


if __name__ == "__main__":
    N, x, y = map(int, input().strip().split())
    tournament(N, x, y)
