import sys

input = sys.stdin.readline


def solution(n):
    dp = [1, 2, 7]
    g = 0
    for i in range(3, n + 1):
        g += 2 * dp[i - 3]
        dp.append((2 * dp[i - 1] + 3 * dp[i - 2] + g) % 1000000007)
    print(dp[n])


if __name__ == "__main__":
    solution(int(input().strip()))
