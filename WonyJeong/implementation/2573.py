import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j, visited):
    stack = [[i, j]]
    union = []
    while stack:
        x, t = stack.pop()

        if visited[x][y] == False:
            visited[x][y] = True
            union.append([x, y])
            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and visited[nx][ny] == False
                    and arr[nx][ny] != 0
                ):
                    stack.append([nx, ny])


def iceLand(N, M, arr, island):
    print(island)

    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            dfs(i, j, visited)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    island = []
    for i in range(N):
        row = list(map(int, input().strip().split()))
        for j in range(M):
            if row[j] != 0:
                island.append([i, j])
