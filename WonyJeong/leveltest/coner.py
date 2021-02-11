# import sys
# from collections import deque

# input = sys.stdin.readline

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


# def solution(board):
#     answer = 0
#     inf = sys.maxsize
#     n = len(board[0])

#     history = [[inf for _ in range(n)] for _ in range(n)]
#     history[0][0] = 0
#     q = deque([[0,0,1],[0,0,2]])

#     while q:
#         bot = q.popleft()
#         x, y, preDiriection = bot

#         for i in range(0, 4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             np = history[x][y] + 100
#             if preDiriection != i:
#                 np += 500

#             if (
#                 0 <= nx < n
#                 and 0 <= ny < n
#                 and np <= history[nx][ny]
#                 and board[nx][ny] != 1
#             ):
#                 q.append([nx, ny, i])
#                 history[nx][ny] = np

#     # return answer
#     return history[n - 1][n - 1]


# if __name__ == "__main__":
#     board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
#     print(solution(board))


import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j, cost, dir):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[i][j] = 1
    q = deque([[i, j, cost, dir]])

    while q:
        bot = q.popleft()
        x, y, pcost, pdir = bot

        if x == n - 1 and y == n - 1:
            answer.append(pcost)
            continue

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            ncost = pcost + 100
            if pdir != i:
                ncost += 500

            if 0 <= nx < n and 0 <= ny < n:
                if not history[nx][ny]:
                    if not visited[nx][ny] or visited[nx][ny] > ncost:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])


def solution(board):
    global n, answer, history, visited
    n = len(board[0])
    answer = []
    history = [board[i][:] for i in range(n)]
    bfs(0, 0, 0, 1)
    bfs(0, 0, 0, 2)

    return min(answer)


if __name__ == "__main__":
    board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
    solution(board)