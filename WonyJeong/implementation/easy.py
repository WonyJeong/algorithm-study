import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def moveDice(side, front, k):
    temp1 = front
    temp2 = side

    temp1[0] = 100

    print(temp)
    print(front)
    # if k == 1:

    return 0


def dice():

    for k in dir_:
        side[3] = map_[x][y]
        front[3] = map_[x][y]

        side, front = moveDice(side, front, k)

        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M:
            x = nx
            y = ny


if __name__ == "__main__":
    global N, M, x, y, K, side, front, map_, dir_
    N, M, x, y, K = map(int, input().strip().split())
    side = deque([0, 0, 0, 0])
    front = deque([0, 0, 0, 0])
    map_ = []
    for _ in range(N):
        map_.append(list(map(int, input().strip().split())))

    dir_ = list(map(int, input().strip().split()))

    dice()
