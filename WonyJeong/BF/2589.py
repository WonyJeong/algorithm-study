import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j, visited):
    q = deque([[i, j, 0]])
    max_ = -1
    while q:
        x, y, dist = q.popleft()
        if visited[x][y] == False:
            visited[x][y] = True
            if max_ < dist:
                max_ = dist
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nDist = dist + 1
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and visited[nx][ny] == False
                    and arr[nx][ny] == "L"
                ):
                    q.append([nx, ny, nDist])
    return max_


def solution(N, M, arr):
    answer = 0
    for i in range(N):
        for j in range(M):
            visited = [[False for _ in range(M)] for _ in range(N)]
            if visited[i][j] == False and arr[i][j] == "L":
                temp = bfs(i, j, visited)
                if answer < temp:
                    answer = temp
    print(answer)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(str, input().strip())))
    solution(N, M, arr)
