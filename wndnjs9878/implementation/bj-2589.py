#2589
import sys
from collections import deque
input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS(i,j):
  queue=deque()
  queue.append((i,j))
  visited=[[0]*M for _ in range(N)]
  visited[i][j]=1
  cnt=0
  while queue:
    x,y = queue.popleft()
    for i in range(4):
        nearX = x + dx[i]
        nearY = y + dy[i]
        if 0 <= nearX < N and 0 <= nearY < M :
            if treasuremap[nearX][nearY]=='L' and visited[nearX][nearY]==0:
                print(x,y)
                print(nearX, nearY)
                visited[nearX][nearY]=visited[x][y]+1
                cnt = max(cnt,visited[nearX][nearY])
                queue.append((nearX,nearY))
    log = cnt - 1
    print(log)
    print('---------------------')
  return log


if __name__ == '__main__':
    N,M=map(int, input().strip().split())
    treasuremap=[list(input().strip()) for _ in range(N)]
    
    result=0
    for i in range(N):
        for j in range(M):
            if treasuremap[i][j]=='L':
                result = max(result,BFS(i,j))

    print(result)