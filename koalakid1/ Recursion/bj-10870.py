import sys

input = sys.stdin.readline

num = int(input())

dp = [0 for _ in range(21)]
dp[1] = 1


def F(num):
    if num == 0 or num == 1:
        return dp[num]
    dp[num] = F(num-2) + F(num-1)
    return dp[num]


print(F(num))
