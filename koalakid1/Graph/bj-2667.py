import sys
from collections import deque


def BFS(graph, x, y):
    queue = deque([(x, y)])

    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]
    count = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            am = a + xm[i]
            bm = b + ym[i]
            if 0 <= am < len(graph) and 0 <= bm < len(graph) and graph[am][bm] == "1":
                graph[am][bm] = "0"
                queue.append((am, bm))
                count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(input()))
    home_count = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "1":
                graph[i][j] = "0"
                home_count.append(BFS(graph, i, j))
    print(len(home_count))
    for i in sorted(home_count):
        print(i)
