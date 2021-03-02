import sys

input = sys.stdin.readline


def solution(N, M):
    memo = [0 for _ in range(M + 1)]
    for i in range(1, N + 1):
        c, p = map(float, input().strip().split())
        c, p = int(c), int(p * 100 + 0.5)
        for j in range(p, M + 1):
            memo[j] = max(memo[j], memo[j - p] + c)

    print(memo[M])


if __name__ == "__main__":
    while True:
        N, M = map(float, input().strip().split())
        if int(N) == 0 and M == 0:
            break
        solution(int(N), int(M * 100))
