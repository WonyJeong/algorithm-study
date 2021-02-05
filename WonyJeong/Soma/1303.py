import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(i, j):
    global arr
    global visited
    global W
    global H

    stack = [[i, j, arr[i][j]]]
    size = 0

    while stack:
        x, y, team = stack.pop()

        if visited[x][y] == False:
            size += 1
            visited[x][y] = True

            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    0 <= nx < H
                    and 0 <= ny < W
                    and visited[nx][ny] == False
                    and team == arr[nx][ny]
                ):
                    stack.append([nx, ny, arr[nx][ny]])

    return size


if __name__ == "__main__":
    W, H = map(int, input().strip().split())
    arr = []
    for _ in range(H):
        arr.append(list(map(str, input().strip())))

    visited = [[False for _ in range(W)] for _ in range(H)]

    answer = [0, 0]

    for i in range(0, H):
        for j in range(0, W):
            if visited[i][j] == False:
                if arr[i][j] == "W":
                    ans = dfs(i, j)
                    answer[0] += ans ** 2
                else:
                    ans = dfs(i, j)
                    answer[1] += ans ** 2
    print(" ".join(map(str, answer)))
