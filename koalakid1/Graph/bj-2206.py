import sys
from collections import deque


def BFS(graph):
    queue = deque([(0, 0, 1)])
    pointer = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    pointer[0][0][1] = 1
    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]
    while queue:
        a, b, c = queue.popleft()
        if a == N-1 and b == M-1:
            return pointer[a][b][c]
        for i in range(4):
            am = a + xm[i]
            bm = b + ym[i]
            if 0 <= am < N and 0 <= bm < M:
                if graph[am][bm] == 1 and c == 1:
                    queue.append((am, bm, 0))
                    pointer[am][bm][0] = pointer[a][b][1] + 1
                elif graph[am][bm] == 0 and pointer[am][bm][c] == 0:
                    queue.append((am, bm, c))
                    pointer[am][bm][c] = pointer[a][b][c] + 1
    return -1


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(BFS(graph))
