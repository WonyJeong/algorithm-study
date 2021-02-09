import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(board):
    answer = 0
    inf = sys.maxsize
    n = len(board[0])
    history = [[inf for _ in range(n)] for _ in range(n)]
    history[0][0] = 0

    temp = []
    if board[0][1] == 0:
        history[0][1] = 100
        temp.append([0, 1, 1])
    if board[1][0] == 0:
        history[1][0] = 100
        temp.append([1, 0, 2])

    q = deque(temp)
    while q:
        bot = q.popleft()
        x, y, preDiriection = bot

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            np = history[x][y] + 100
            if preDiriection != i:
                np += 500

            if (
                0 <= nx < n
                and 0 <= ny < n
                and np <= history[nx][ny]
                and board[nx][ny] != 1
            ):
                q.append([nx, ny, i])
                history[nx][ny] = np

    # return answer
    return history[n - 1][n - 1]


if __name__ == "__main__":
    board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    print(solution(board))
