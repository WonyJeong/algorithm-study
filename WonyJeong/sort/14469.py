import sys

input = sys.stdin.readline


def solution(N, cows):
    cows = sorted(cows, key=lambda x: (x[0], x[1]))
    for i in range(1, N):
        x, y = cows[i - 1]
        nx, ny = cows[i]
        if x + y > nx:
            cows[i][0] = x + y
    print(cows[-1][0] + cows[-1][1])


if __name__ == "__main__":
    N = int(input().strip())
    cows = []
    for _ in range(N):
        cows.append(list(map(int, input().strip().split())))
    solution(N, cows)
