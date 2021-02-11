#7569
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]


def BFS(tomato,start):
    totalDays = 0

    while len(start) > 0 :
        node = start.popleft()
        z, y, x= node[0], node[1], node[2]
        # print(z,y,x)
        for k in range(6) :
            nearX = x + dx[k]
            nearY = y + dy[k]
            nearZ = z + dz[k]

            if 0 <= nearX < M and 0 <= nearY < N and 0 <= nearZ < H:
                if tomato[nearZ][nearY][nearX] == 0: #안익은 토마토!
                    tomato[nearZ][nearY][nearX] = tomato[z][y][x]+1 #익을수 있다!
                    start.append([nearZ,nearY, nearX])
                    totalDays = tomato[nearZ][nearY][nearX] -1
                    # print(totalDays)

    # for page in tomato:
    #     for row in page:
    #         for element in row:
    #             print(element, end='')
    #         print()
    #     print("-------------------")

    for row in tomato:
        for element in row:
            if 0 in element :
                # print('0 exist!!!!!')
                return -1
    
    return totalDays

if __name__ == '__main__':
    M, N, H = map(int, input().strip().split())
    tomato = [[list(map(int,input().strip().split())) for _ in range(N)] for _ in range(H)]
    start = deque()
  
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    start.append([i,j,k])

    # for page in tomato:
    #     for row in page:
    #         for element in row:
    #             print(element, end='')
    #         print()
    #     print("-------------------")
    
    # print(start)
    print(BFS(tomato, start))
