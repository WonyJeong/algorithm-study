import sys

input = sys.stdin.readline


def knapSack(N, K):

    memo = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    item = [list(map(int, input().strip().split())) for _ in range(N)]

    for i in range(1, N + 1):
        w = item[i - 1][0]
        v = item[i - 1][1]
        if i == 1:
            for j in range(w, K + 1):
                memo[i][j] = v
        else:
            # memo[i] = memo[i - 1]
            for j in range(0, K + 1):
                if w <= j:
                    memo[i][j] = max(v + memo[i - 1][j - w], memo[i - 1][j])
                else:
                    memo[i][j] = memo[i - 1][j]
    # print(memo)
    print(max(memo[N]))


if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    knapSack(N, K)
