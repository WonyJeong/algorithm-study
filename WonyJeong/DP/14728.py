import sys

input = sys.stdin.readline


def solution(arr, T):
    dp = [[0 for _ in range(T + 1)] for _ in range(len(arr) + 1)]

    for i in range(1, len(arr) + 1):
        time, score = arr[i - 1]
        for j in range(T + 1):
            if time <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + score)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[len(arr)][T])


if __name__ == "__main__":
    N, T = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(arr, T)
