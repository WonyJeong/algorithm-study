import sys

input = sys.stdin.readline

N,M = map(int,input().strip().split())
cards = list(map(int,input().strip().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sumVal = cards[i] + cards[j] + cards[k]
            if sumVal <= M:
                result = max(result, sumVal)
print(result)