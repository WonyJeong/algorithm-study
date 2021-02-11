#2206
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(N, M, wallmap):
    queue = deque()
    queue.append([0,0,0])
    '''
    각 지점마다 벽을 부쉈을 때 최단거리, 벽을 안부쉈을 때의 최단거리를 구해줘야함
-> 3차원이 flag같은 개념으로 사용됨
    '''
    visited = [[[0]*M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    while len(queue) > 0:
        node = queue.popleft()
        x, y, wall = node[2], node[1], node[0] # wall: 벽 부쉈는지 여부 0:안부심, 1:부심
        if x == (M-1) and y == (N-1):
            # from pprint import pprint
            # pprint(visited)
            return visited[wall][N-1][M-1]
        for k in range(4):
            nearX = x + dx[k]
            nearY = y + dy[k]
            if 0 <= nearX < M and 0<= nearY < N and visited[wall][nearY][nearX] == 0:
                if wallmap[nearY][nearX] == 0 :
                    queue.append([wall, nearY, nearX])
                    visited[wall][nearY][nearX] = visited[wall][y][x] + 1

                elif wallmap[nearY][nearX] == 1 and wall == 0:
                    queue.append([1,nearY, nearX])
                    visited[1][nearY][nearX] = visited[0][y][x] +1
    return -1


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    wallmap = [ list(map(int, input().strip())) for _ in range(N)]

    print(BFS(N, M, wallmap))