import sys

input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def moveDice(side, front, k):
    if k == 1:
        front_ = [front[0], side[0], front[2], side[2]]
        side_ = [front[3], side[0], side[1]]
    elif k == 2:
        front_ = [front[0], side[2], front[2], side[0]]
        side_ = [side[1], side[2], front[3]]
    elif k == 3:
        front_ = [front[1], front[2], front[3], front[0]]
        side_ = [side[0], front[2], side[2]]
    elif k == 4:
        front_ = [front[3], front[0], front[1], front[2]]
        side_ = [side[0], front[0], side[2]]

    return side_, front_


def dice(x, y):
    front = [0, 0, 0, 0]
    side = [0, 0, 0]

    for k in dir_:
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if map_[x][y] != 0:
                front[3] = map_[x][y]
                map_[x][y] = 0
            else:
                map_[x][y] = front[3]

            if 0 <= nx < N and 0 <= ny < M:
                side, front = moveDice(side, front, k)
                x = nx
                y = ny
                print(front[1])


if __name__ == "__main__":
    global N, M, K, map_, dir_
    N, M, x, y, K = map(int, input().strip().split())
    map_ = []
    for _ in range(N):
        map_.append(list(map(int, input().strip().split())))
    dir_ = list(map(int, input().strip().split()))
    dice(x, y)
