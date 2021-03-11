import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def drawMap(N, area, i, j):
    numOfCows = 0
    stack = [[i, j]]
    parm[i][j] = area
    while stack:
        x, y = stack.pop()
        numOfCows += cows[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not [x, y, nx, ny] in bridge:
                if 0 <= nx < N and 0 <= ny < N and parm[nx][ny] == -1:
                    parm[nx][ny] = area
                    stack.append([nx, ny])
    return numOfCows


def solution(N):
    global parm
    parm = [[-1 for _ in range(N)] for _ in range(N)]
    count = []
    area = 0
    for i in range(N):
        for j in range(N):
            if parm[i][j] == -1:
                count.append(drawMap(N, area, i, j))
                area += 1

    answer = 0
    for i in range(len(count) - 1):
        temp = count[i]
        temp2 = 0
        for j in range(i + 1, len(count)):
            temp2 += count[j]
        answer += temp * temp2

    print(answer)


if __name__ == "__main__":
    global cows, bridge
    N, M, K = map(int, input().strip().split())
    bridge = []
    cows = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z, w = map(int, input().strip().split())
        bridge.append([x - 1, y - 1, z - 1, w - 1])
        bridge.append([z - 1, w - 1, x - 1, y - 1])

    for _ in range(K):
        i, j = map(int, input().strip().split())
        cows[i - 1][j - 1] = 1
    solution(N)