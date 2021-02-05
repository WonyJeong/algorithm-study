#2798
import sys
input = sys.stdin.readline
def solved(N,M,cards) :
    maxSum = 0
    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if cards[i] + cards[j] + cards[k] > M:
                    continue
                else:
                    maxSum = max(maxSum, cards[i] + cards[j] + cards[k])
    return maxSum


if __name__ == "__main__":
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    print(solved(N,M,cards))