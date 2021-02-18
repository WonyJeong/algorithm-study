import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(shark, eatable):
    result = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([[shark[0], shark[1], shark[2], 0]])
    while q:
        x, y, w, d = q.popleft()
        if visited[x][y] == False:
            if [x, y, arr[x][y]] in eatable:
                if len(result) > 0 and result[len(result) - 1][2] < d:
                    return result
                else:
                    result.append([x, y, d])

            visited[x][y] = True
            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= w:
                    q.append([nx, ny, w, d + 1])

    return result


def babyShark(N, arr, fish, shark):
    fish = sorted(fish, key=lambda x: (x[2], x[0], x[1]))
    exp = 0
    eatable = []
    answer = 0

    while True:
        for i, j, w in fish:
            if w < shark[2]:
                eatable.append([i, j, w])
        eatablePostion = bfs(shark, eatable)
        if eatablePostion:
            eatablePostion = sorted(eatablePostion, key=lambda x: (x[2], x[0], x[1]))
            # print("eatable Position : ", eatablePostion)
            x, y, d = eatablePostion[0]
            shark[0] = x
            shark[1] = y
            arr[x][y] = 0
            answer += d
            exp += 1
            if exp == shark[2]:
                exp = 0
                shark[2] += 1
        else:
            break

    print(answer)


if __name__ == "__main__":
    global arr, N
    N = int(input().strip())
    arr = []
    fish = []
    for i in range(N):
        row = list(map(int, input().strip().split()))
        for j in range(N):
            if row[j] == 9:
                shark = [i, j, 2]
                row[j] = 0
            elif row[j] != 0:
                fish.append([i, j, row[j]])

        arr.append(row)

    babyShark(N, arr, fish, shark)
