#2798
def solved(N,M,cards) :
    sum = 0
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if cards[i] + cards[j] + cards[k] > M:
                    continue
                else:
                        sum = max(sum, cards[i] + cards[j] + cards[k])
    return sum


if __name__ == "__main__":
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    print(solved(N,M,cards))