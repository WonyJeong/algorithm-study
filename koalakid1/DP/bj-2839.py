import sys
input = sys.stdin.readline
n = int(input())

if n <= 5:
    print((n == 3 or n == 5) and 1 or -1)

else:
    dp = [9999 for i in range(n+1)]
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)

    if dp[n] > 9999:
        print(-1)
    else:
        print(dp[n])
