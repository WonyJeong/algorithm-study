from collections import deque
import sys


def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)

            if n in graph:
                roots = list(set(graph[n]) - set(visited))
                roots.sort(reverse=True)
                stack += roots
    return " ".join(str(i) for i in visited)


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)

            if n in graph:
                roots = list(set(graph[n]) - set(visited))
                roots.sort()
                queue += roots
    return " ".join(str(i) for i in visited)


input = sys.stdin.readline
graph = {}
node, edge, start = map(int, input().strip().split())

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
print(graph)
print(DFS(graph, start))
print(BFS(graph, start))
