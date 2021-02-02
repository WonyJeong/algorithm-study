import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def tomato(N, M, arr, q):
    visited = [[False for _ in range(N)] for _ in range(M)]

    while q:
        bot = q.popleft()
        x = bot[0]
        y = bot[1]
        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(0, 4):
                if (
                    0 <= x + dx[i] < M
                    and 0 <= y + dy[i] < N
                    and visited[x + dx[i]][y + dy[i]] == False
                ):
                    if arr[x + dx[i]][y + dy[i]] == 0:
                        arr[x + dx[i]][y + dy[i]] = arr[x][y] + 1
                        q.append([x + dx[i], y + dy[i]])

    flag = False
    for i in range(0, M):
        for j in range(0, N):
            if arr[i][j] == 0:
                flag = True
                break

    if flag == True:
        print(-1)
    else:
        print(max(map(max, arr)) - 1)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    q = deque()
    for i in range(0, M):
        row = list(map(int, input().strip().split()))
        for j in range(0, N):
            if row[j] == 1:
                q.append([i, j])
        arr.append(row)

    tomato(N, M, arr, q)
