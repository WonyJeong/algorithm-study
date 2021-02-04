import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    drinks = [int(input()) for _ in range(N)]
    dp = [0 for _ in range(N+1)]

    if N <= 2:
        print(sum(drinks))
    else:
        dp[0:3] = [0, drinks[0], drinks[0]+drinks[1]]
        for i in range(3, N+1):
            dp[i] = max(dp[i-1], drinks[i-1] + dp[i-2],
                        drinks[i-1] + drinks[i-2] + dp[i-3])
        print(dp[N])
