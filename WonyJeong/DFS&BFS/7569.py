import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def tomato(N, M, T, arr, q):
    visited = [[[False for _ in range(N)] for _ in range(M)] for _ in range(T)]
    max = 0

    if len(q) == N * M * T:
        print(max)
        return

    while q:
        bot = q.popleft()
        x = bot[1]
        y = bot[2]
        z = bot[0]
        if visited[z][x][y] == False:
            visited[z][x][y] = True
            for i in range(0, 6):
                dx_ = x + dx[i]
                dy_ = y + dy[i]
                dz_ = z + dz[i]
                if (
                    0 <= dx_ < M
                    and 0 <= dy_ < N
                    and 0 <= dz_ < T
                    and visited[dz_][dx_][dy_] == False
                ):
                    if arr[dz_][dx_][dy_] == 0:
                        arr[dz_][dx_][dy_] = arr[z][x][y] + 1
                        if max <= arr[dz_][dx_][dy_]:
                            max = arr[dz_][dx_][dy_]
                        q.append([dz_, dx_, dy_])
    for k in range(0, T):
        for i in range(0, M):
            for j in range(0, N):
                if arr[k][i][j] == 0:
                    print(-1)
                    return

    print(max - 1 if max != 0 else max)


if __name__ == "__main__":
    N, M, T = map(int, input().strip().split())
    arr = []
    q = deque()

    for t in range(0, T):
        temp = []
        for i in range(0, M):
            row = list(map(int, input().strip().split()))
            for j in range(0, N):
                if row[j] == 1:
                    q.append([t, i, j])
            temp.append(row)
        arr.append(temp)

    tomato(N, M, T, arr, q)