import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().strip().split()))
prices = list(map(int, input().strip().split()))

result = 0
price = 0
distance = 0
for i in range(N-1):
    if i == 0:
        price = prices[i]
        distance = distances[i]
    else:
        if price <= prices[i]:
            distance += distances[i]
        else:
            result += price * distance
            price = prices[i]
            distance = distances[i]
print(result + price * distance)
