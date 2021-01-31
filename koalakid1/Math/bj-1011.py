import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().strip().split())

    distance = y-x
    root = math.floor(math.sqrt(distance))

    maxVal = (root+1)**2
    minVal = root**2

    if distance == minVal:
        print(root*2 - 1)
    elif distance <= minVal + (maxVal-minVal)//2:
        print(root*2)
    else:
        print(root*2 + 1)
