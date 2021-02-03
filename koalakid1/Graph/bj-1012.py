import sys
from collections import deque


def BFS(graph, x, y):
    queue = deque([(x, y)])

    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            am = a + xm[i]
            bm = b + ym[i]
            if 0 <= am < N and 0 <= bm < M and graph[am][bm] == 1:
                graph[am][bm] = 0
                queue.append((am, bm))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        graph = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().strip().split())
            graph[y][x] = 1

        count = 0

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    BFS(graph, i, j)
                    count += 1

        print(count)
