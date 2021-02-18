import sys
from itertools import product

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
## ㅅㅂ 몬하겟다


def getArea(N, M, arr, cctv):
    for i in range(len(cctv)):
        x, y, z = cctv[i]
        for j in range(4):
            while 0 <= x < N and 0 <= y < M and arr[x][y] != 6:
                x += dx[j]
                y += dy[j]


def solution(N, M, arr, cctv, cctv5):
    for i, j in cctv5:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
                if 1 <= arr[nx][ny] <= 5:
                    nx += dx[k]
                    ny += dy[k]
                    continue
                arr[nx][ny] = "#"
                nx += dx[k]
                ny += dy[k]
    temp = [[arr[i][j] for j in range(M)] for i in range(N)]

    for v in product(range(4), range(4)):
        print(v)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = []
    cctv = []
    cctv5 = []
    for i in range(N):
        row = list(map(int, input().strip().split()))
        for j in range(M):
            if 0 < row[j] < 5:
                cctv.append([i, j, row[j]])
            elif row[j] == 5:
                cctv5.append([i, j])
        arr.append(row)
    solution(N, M, arr, cctv, cctv5)
