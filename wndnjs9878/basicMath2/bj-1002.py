#1002
import sys
import math
input = sys.stdin.readline

def solution(x1, y1, r1, x2, y2, r2):

    distance = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))

    if x1==x2 and y1==y2:
        if r1==r2:
            return (-1)
        else:
            return (0)
    
    elif r1+r2 == distance or abs(r2-r1) == distance:
        return (1)

    elif r1 + r2 < distance or distance < abs(r2-r1):
        return (0)
    else:
        return (2)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
        print(solution(x1, y1, r1, x2, y2, r2))
    