#1011
import sys
input = sys.stdin.readline

def solved(x,y):
    remainDistance = y-x
    movingCount = 0
    movedDistance = 1 #처음엔 무조건 1만큼 이동
    while remainDistance > 0:
        remainDistance -= movedDistance
        if movingCount%2 == 1:
            movedDistance += 1            
        movingCount += 1
    return (movingCount)

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(0, T):
        x, y = map(int, input().strip().split())
        print(solved(x,y))