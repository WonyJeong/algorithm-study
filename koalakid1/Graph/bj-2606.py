import sys
from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        q = queue.popleft()
        if q not in visited:
            visited.append(q)
            if q in graph:
                roots = list(set(graph[q]) - set(visited))
                roots.sort()
                queue += roots
    return len(visited) - 1


if __name__ == "__main__":
    input = sys.stdin.readline
    graph = {}
    node = int(input())
    edge = int(input())

    for _ in range(edge):
        n1, n2 = map(int, input().strip().split())

        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n2 not in graph[n2]:
            graph[n2].append(n1)

    print(BFS(graph, 1))
