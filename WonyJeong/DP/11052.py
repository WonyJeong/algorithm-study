import sys

input = sys.stdin.readline


def solution(n, card):
    memo = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = card[i - 1]

        for j in range(i, n + 1):
            memo[j] = max(memo[j], memo[j - i] + price)
    print(memo[n])


if __name__ == "__main__":
    N = int(input().strip())
    card = list(map(int, input().strip().split()))
    solution(N, card)
