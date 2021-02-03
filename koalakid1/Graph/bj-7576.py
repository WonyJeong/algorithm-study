import sys
from collections import deque


def BFS(graph):
    xm = [1, -1, 0, 0, 0, 0]
    ym = [0, 0, 1, -1, 0, 0]
    zm = [0, 0, 0, 0, 1, -1]
    while queue:
        c, b, a = queue.popleft()
        for i in range(6):
            am = a + xm[i]
            bm = b + ym[i]
            cm = c + zm[i]
            if 0 <= am < M and 0 <= bm < N and 0 <= cm < H and graph[cm][bm][am] == 0:
                queue.append((cm, bm, am))
                graph[cm][bm][am] = graph[c][b][a] + 1


if __name__ == "__main__":
    M, N, H = map(int, input().strip().split())
    graph = [[list(map(int, input().strip().split()))
              for _ in range(N)] for _ in range(H)]
    queue = deque()
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    queue.append((z, y, x))

    BFS(graph)
    result = 1
    for i in graph:
        if result == 0:
            break
        for j in i:
            if result == 0:
                break
            for k in j:
                if k == 0:
                    result = 0
                    break
                result = max(result, k)
    print(result - 1)
