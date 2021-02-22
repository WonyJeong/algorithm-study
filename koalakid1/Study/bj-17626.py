import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    m = int(n ** (1/2))
    sq = [i ** 2 for i in range(m, 0, -1)]
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        j = 1
        minv = 4
        while j ** 2 <= i:
            minv = min(minv, dp[i-j**2])
            j += 1
        dp[i] = minv + 1
    print(dp[n])
