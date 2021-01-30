import sys

input = sys.stdin.readline

num = int(input())

nowRoom = 1
maxVal = 0
while True:
    if nowRoom == 1:
        maxVal = 1
        nowRoom += 1
        if num == maxVal:
            print(1)
            break
    else:
        maxVal += 6 * (nowRoom - 1)
        if num <= maxVal:
            print(nowRoom)
            break
        nowRoom += 1
