import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    item = list(map(int, input().strip().split()))

    all = 0
    count = 0
    for i in range(len(item)):
        if i == 0:
            count = item[i]
        else:
            all += item[i]

    aver = all/count

    count2 = 0
    for i in range(1, count+1):
        if aver < item[i]:
            count2 += 1
    print('%.3f%%' % (count2 / count * 100))
