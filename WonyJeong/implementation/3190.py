import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def snake():
    answer = 0
    q = deque([[0, 0]])
    cursor = 0
    dirIndex = 1
    time, dir_ = direction[cursor]
    delApple = []

    while True:
        answer += 1
        x, y = q[len(q) - 1]
        nx = x + dx[dirIndex]
        ny = y + dy[dirIndex]

        if 0 <= nx < N and 0 <= ny < N and not [nx, ny] in q:
            q.append([nx, ny])
            if not [nx + 1, ny + 1] in apple:
                q.popleft()
            else:
                del apple[apple.index([nx + 1, ny + 1])]

        else:
            print(answer)
            break

        if answer == int(time) and cursor < L:
            if dir_ == "L":
                dirIndex = (dirIndex + 3) % 4
            else:
                dirIndex = (dirIndex + 1) % 4

            cursor += 1
            if cursor < L:
                time, dir_ = direction[cursor]


if __name__ == "__main__":
    global N, K, apple, direction, L
    N = int(input().strip())
    K = int(input().strip())
    apple = []
    direction = []
    for _ in range(K):
        apple.append(list(map(int, input().strip().split())))
    L = int(input().strip())
    for _ in range(L):
        direction.append(list(map(str, input().strip().split())))

    snake()
