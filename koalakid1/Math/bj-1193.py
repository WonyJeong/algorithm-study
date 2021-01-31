import sys

input = sys.stdin.readline

num = int(input())

nowSection = 1
maxCount = 0
while True:
    maxCount += nowSection
    if num <= maxCount:
        row = maxCount - num
        if nowSection % 2 == 0:
            print(f'{nowSection - row}/{row + 1}')

        else:
            print(f'{row + 1}/{nowSection - row}')
        break
    else:
        nowSection += 1
