import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())

coin = []
for i in range(N):
    coin.append(int(input()))

count = 0
for c in sorted(coin, reverse=True):
    count += K//c
    K %= c
    if K == 0:
        break
print(count)
