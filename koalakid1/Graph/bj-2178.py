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
            if 0 <= am < N and 0 <= bm < M and graph[am][bm] == 1 and ~check[am][bm]:
                queue.append((am, bm))
                check[am][bm] = True
                graph[am][bm] = graph[a][b] + 1


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    check = [[False for _ in range(M)] for _ in range(N)]
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(input().strip()))))
    check[0][0] = True
    BFS(graph, 0, 0)
    print(graph[N-1][M-1])
