import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j, h, visited):
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > h:
                    q.append([nx, ny])


def solution(N, H, arr):
    answer = 1
    for h in range(1, H + 1):
        visited = [[False for _ in range(N)] for _ in range(N)]
        temp = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False and arr[i][j] > h:
                    bfs(i, j, h, visited)
                    temp += 1
        if answer < temp:
            answer = temp

    print(answer)


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    max_ = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        max_.append(max(row))
        arr.append(row)
    solution(N, max(max_), arr)
