import sys

input = sys.stdin.readline

from collections import deque


dx = [-1, +1, +2, +2, +1, -1, -2, -2]
dy = [-2, -2, -1, +1, +2, +2, -1, +1]


def knight(l, cur, goal):
    q = deque([cur])
    gx = goal[0]
    gy = goal[1]
    visited = [[-1 for _ in range(l)] for _ in range(l)]
    flag = True

    visited[cur[0]][cur[1]] = 0

    if cur == goal:
        print(0)
        return

    while flag and q:

        bot = q.popleft()
        x = bot[0]
        y = bot[1]

        if visited[x][y] >= 0:
            for i in range(0, 8):
                if (
                    0 <= x + dx[i] < l
                    and 0 <= y + dy[i] < l
                    and visited[x + dx[i]][y + dy[i]] == -1
                ):
                    visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1

                    if [x + dx[i], y + dy[i]] == goal:
                        print(visited[gx][gy])
                        flag = False

                    q.append([x + dx[i], y + dy[i]])

    return


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(0, T):
        l = int(input().strip())
        cur = list(map(int, input().strip().split()))
        goal = list(map(int, input().strip().split()))

        knight(l, cur, goal)
