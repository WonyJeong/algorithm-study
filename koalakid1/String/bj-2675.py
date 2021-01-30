import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    count, string = map(str, input().strip().split())
    count = int(count)

    for i in string:
        print(i*count, end="")
    print("")
