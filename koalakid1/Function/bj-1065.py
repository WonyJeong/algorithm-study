import sys


def hansu(a):
    b = str(a)
    distance = []
    prev = -1
    for i in b:
        i = int(i)
        if prev < 0:
            prev = i
        else:
            distance.append(i-prev)
            prev = i

    return 1 if distance.count(distance[0]) == 2 else 0


input = sys.stdin.readline

num = int(input())

if num <= 99:
    print(num)
else:
    count = 99
    for i in range(111, num+1):
        count += hansu(i)
    print(count)
