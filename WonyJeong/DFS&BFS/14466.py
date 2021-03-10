import sys
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def drawMap(N, area, i, j):
    stack = [[i, j]]
    parm[i][j] = area
    while stack:
        x, y = stack.pop()
        if parm[x][y] == area:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not tuple([nx, ny]) in bridge[x][y]:
                    if 0 <= nx < N and 0 <= ny < N and parm[nx][ny] == -1:
                        parm[nx][ny] = area
                        stack.append([nx, ny])


def solution(N, bridges, cows):
    global parm, bridge
    answer = 0
    area = 0
    parm = [[-1 for _ in range(N)] for _ in range(N)]
    bridge = [[set() for _ in range(N)] for _ in range(N)]

    for x, y, z, w in bridges:
        bridge[x][y].add(tuple([z, w]))
        bridge[z][w].add(tuple([x, y]))

    for i in range(N):
        for j in range(N):
            if parm[i][j] == -1:
                drawMap(N, area, i, j)
                area += 1

    for comb in combinations(cows, 2):
        u, v = list(comb)
        x, y = u[0] - 1, u[1] - 1
        z, w = v[0] - 1, v[1] - 1

        if parm[x][y] != parm[z][w]:
            print(u, v, " 는 반드시 다리를 건너야만 만날 수 있다.")
            answer += 1
    for p in parm:
        print(p)
    print(answer)


if __name__ == "__main__":
    N, M, K = map(int, input().strip().split())
    bridge = []
    cows = []
    for _ in range(M):
        x, y, z, w = map(int, input().strip().split())
        bridge.append([x - 1, y - 1, z - 1, w - 1])
    for _ in range(K):
        cows.append(list(map(int, input().strip().split())))
    solution(N, bridge, cows)
