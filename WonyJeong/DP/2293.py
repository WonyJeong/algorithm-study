import sys
import math

input = sys.stdin.readline


def solution(coins, m):
    memo = [0 for i in range(m + 1)]
    memo[0] = 1
    for coin in coins:
        for i in range(coin, m + 1):
            memo[i] += memo[i - coin]

    print(memo[m])


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    coins = []
    for _ in range(N):
        coins.append(int(input().strip()))
    solution(coins, M)
