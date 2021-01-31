import sys

input = sys.stdin.readline

while True:
    item = list(map(int, input().strip().split()))
    if sum(item) == 0:
        break
    maxVal = max(item)
    item.remove(maxVal)
    if item[0]**2 + item[1]**2 == maxVal**2:
        print("right")
    else:
        print("wrong")
