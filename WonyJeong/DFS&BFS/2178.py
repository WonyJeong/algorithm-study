import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def maze(N, M, arr):
    visited = [[False for _ in range(M)] for _ in range(N)]
    history = [[0 for _ in range(M)] for _ in range(N)]
    history[0][0] = 1
    q = deque([[0, 0]])

    flag = True

    while q and flag:
        bot = q.popleft()
        x = bot[0]
        y = bot[1]
        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(0, 4):
                if (
                    0 <= x + dx[i] < N
                    and 0 <= y + dy[i] < M
                    and arr[x + dx[i]][y + dy[i]] == 1
                    and visited[x + dx[i]][y + dy[i]] == False
                ):
                    history[x + dx[i]][y + dy[i]] = history[x][y] + 1

                    if x + dx[i] == N - 1 and y + dy[i] == M - 1:
                        flag = False

                    q.append([x + dx[i], y + dy[i]])

    print(history[N - 1][M - 1])


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip())))

    maze(N, M, arr)
