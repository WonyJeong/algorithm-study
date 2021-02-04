import sys
from collections import deque


def BFS(graph):

    queue = deque([])

    visited = [0 for _ in range(V+1)]
    Start = True
    for i in range(1, V+1):
        if not Start:
            break
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
        while queue and Start:
            x = queue.popleft()
            for y in graph[x]:
                if visited[x] == visited[y]:
                    Start = False
                elif visited[y] == 0:
                    visited[y] = 3 - visited[x]
                    queue.append(y)
    if Start:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    input = sys.stdin.readline
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().strip().split())

        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            x, y = map(int, input().strip().split())
            graph[x].append(y)
            graph[y].append(x)
        BFS(graph)
