import sys
from collections import deque
input = sys.stdin.readline

def knight(x,y,a,b):
    global graph
    global l
    queue = deque([(x,y,0)])
    xm = [1,1,-1,-1]
    ym = [1,-1,1,-1]
    while queue:
        x,y,w = queue.popleft()

        if x == a and y == b:
            print(w)
            break

        for i in range(1,3):
            for j in range(4):
                xn = x + (i % 2 + 1) * xm[j]
                yn = y + i * ym[j]
                if 0 <= xn < l and 0 <= yn < l and graph[xn][yn]:
                    graph[xn][yn] = False
                    queue.append((xn,yn,w+1))

        


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        l = int(input())
        x,y = map(int,input().strip().split())
        a,b = map(int,input().strip().split())
        
        graph = [[False if (i == x and j == y) else True for j in range(l)] for i in range(l)]
        
        knight(x,y,a,b)
