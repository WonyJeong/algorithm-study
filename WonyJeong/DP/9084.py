import sys

input = sys.stdin.readline


def solution(N, coins, money):
    memo = [0 for _ in range(money + 1)]
    memo[0] = 1
    for i in range(len(coins)):
        coin = coins[i - 1]
        for j in range(coin, money + 1):
            memo[j] += memo[j - coin]

    print(memo[money])


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        coins = list(map(int, input().strip().split()))
        money = int(input().strip())
        solution(N, coins, money)
