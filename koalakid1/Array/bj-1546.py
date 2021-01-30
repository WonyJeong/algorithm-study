import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    n = input().strip()

    count = 1
    result = 0
    for i in n:
        if i == "O":
            result += 1 * count
            count += 1
        else:
            count = 1
    print(result)
