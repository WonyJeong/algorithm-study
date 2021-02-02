import sys
input = sys.stdin.readline
n = int(input())

result = []
for i in range(n):
    R, G, B = map(int, input().strip().split())
    if i == 0:
        result.append([R, G, B])
    else:
        R += min(result[i-1][1], result[i-1][2])
        G += min(result[i-1][0], result[i-1][2])
        B += min(result[i-1][1], result[i-1][0])
        result.append([R, G, B])

print(min(result[n-1]))
