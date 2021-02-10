#7562
import sys
from collections import deque
input = sys.stdin.readline

dx = [+1, +2, -1, -2, +1, +2, -1, -2]
dy = [+2, +1, +2, +1, -2, -1, -2, -1]

def BFS(l, nowRow, nowCol, wantRow, wantCol):
    queue = deque()
    queue.append([nowRow, nowCol])
    visited = [[0]*l for _ in range(l)]

    while len(queue) > 0:
        position = queue.popleft()
        x,y = position[0], position[1]
        if x == wantRow and y == wantCol :
            return visited[x][y]
        for k in range(8):
            movedX = x + dx[k]
            movedY = y + dy[k]
            if 0 <= movedX < l and 0<= movedY < l and visited[movedX][movedY] == 0:
                queue.append([movedX, movedY])
                visited[movedX][movedY] = visited[x][y] +1



if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        l = int(input().strip())
        nowRow, nowCol = map(int, input().strip().split())
        wantRow, wantCol = map(int, input().strip().split())
        print(BFS(l, nowRow, nowCol, wantRow, wantCol))