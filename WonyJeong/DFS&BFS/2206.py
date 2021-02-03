import sys

input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(N, M, map_):
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    history = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    # history[0] 은 벽을 안부수고 간 기록
    end = [M - 1, N - 1]
    q = deque([[0, 0, 0]])

    while q:

        bot = q.popleft()
        f = bot[0]
        x = bot[1]
        y = bot[2]

        if x == N - 1 and y == M - 1:
            print(history[f][x][y] + 1)
            return

        if visited[f][x][y] == False:
            visited[f][x][y] = True
            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visited[f][nx][ny] == False:
                    if map_[nx][ny] == 1 and f == 0:
                        history[1][nx][ny] = history[0][x][y] + 1
                        q.append([1, nx, ny])
                    elif map_[nx][ny] == 0:
                        history[f][nx][ny] = history[f][x][y] + 1
                        q.append([f, nx, ny])
    print(-1)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    map_ = []
    for _ in range(0, N):
        row = list(map(int, input().strip()))
        map_.append(row)

    bfs(N, M, map_)
