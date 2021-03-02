import sys

input = sys.stdin.readline


def solution(N, w, p):
    memo = [[0 for _ in range(100)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        weigh = w[i - 1]
        price = p[i - 1]
        if i == 1:
            for j in range(weigh, 100):
                memo[i][j] = price
        else:
            for j in range(0, 100):
                if j >= weigh:
                    memo[i][j] = max(memo[i - 1][j - weigh] + price, memo[i - 1][j])
                else:
                    memo[i][j] = memo[i - 1][j]
    print(memo[N][99])


if __name__ == "__main__":
    N = int(input().strip())
    w = list(map(int, input().strip().split()))
    p = list(map(int, input().strip().split()))
    solution(N, w, p)
