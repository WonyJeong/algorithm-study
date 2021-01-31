import sys

input = sys.stdin.readline

num = int(input())

num_h = {}

for i in range(1, 15):
    num_h[(0, i)] = i

for i in range(1, 15):
    for j in range(1, 15):
        count = 0
        for l in range(1, j+1):
            count += num_h[(i-1, l)]
        num_h[(i, j)] = count

for _ in range(num):
    k = int(input())
    n = int(input())
    print(num_h[k, n])
