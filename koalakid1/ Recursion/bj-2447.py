import sys

input = sys.stdin.readline

num = int(input())

page = [[0 for _ in range(num)] for _ in range(num)]


def printStar(n):
    if n == 3:
        page[0][:3] = page[2][:3] = [1, 1, 1]
        page[1][0:3] = [1, 0, 1]
        return
    a = n // 3
    printStar(a)

    for i in range(3):
        for j in range(3):
            if i == j == 0 or i == j == 1:
                continue
            for l in range(a):
                page[a*i+l][a*j:a*(j+1)] = page[l][:a]


printStar(num)

for i in page:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
