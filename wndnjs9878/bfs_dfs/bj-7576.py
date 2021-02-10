#7576
import sys
from collections import deque
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def BFS(tomato,start):
    totalDays = 0

    while len(start) > 0 :
        node = start.popleft()
        y, x= node[0], node[1]
        # print(y,x)
        for k in range(4) :
            nearX = x + dx[k]
            nearY = y + dy[k]

            if 0 <= nearX < M and 0 <= nearY < N:
                if tomato[nearY][nearX] == 0: #안익은 토마토!
                    tomato[nearY][nearX] = tomato[y][x]+1 #익을수 있다!
                    start.append([nearY, nearX])
                    totalDays = tomato[nearY][nearX] -1


    # for element in tomato:
    #      print(element)


    for element in tomato:
        if 0 in element :
            return -1
    
    return totalDays

if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    tomato = []
    start = deque()
    for i in range(N):
        row = list(map(int,(input().strip().split())))
        for j in range(M):
            if row[j] == 1:
                start.append([i,j])
        tomato.append(row)

    print(BFS(tomato, start))

    
