import sys

input = sys.stdin.readline


def getPrice(T, dist, prices):
    answer = 0

    price = prices[0]
    for i in range(1, T):
        if prices[i] > price:
            prices[i] = price
        else:
            price = prices[i]

    for i in range(0, T - 1):
        answer += dist[i] * prices[i]

    print(answer)


if __name__ == "__main__":
    T = int(input().strip())
    dist = list(map(int, input().strip().split()))
    prices = list(map(int, input().strip().split()))
    getPrice(T, dist, prices)
