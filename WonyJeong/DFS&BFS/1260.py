import sys
from collections import deque

input = sys.stdin.readline


def dfs(N, M, V, _graph):
    graph = _graph
    answer = []

    stack = [V]
    visited = [False] * (N + 1)

    while stack:
        top = stack.pop()
        if visited[top] == False:
            visited[top] = True
            answer.append(top)
            if top in graph.keys():
                child = sorted(graph[top], reverse=True)
                # del graph[top]
                stack += child

    print(" ".join(map(str, answer)))


def bfs(N, M, V, _graph):
    graph = _graph
    answer = []
    visited = [False] * (N + 1)
    q = deque([V])

    while q:
        bot = q.popleft()
        if visited[bot] == False:
            visited[bot] = True
            answer.append(bot)
            if bot in graph.keys():
                child = sorted(graph[bot])
                # del graph[bot]
                q += child

    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    graph = {}
    N, M, V = map(int, input().strip().split())
    for _ in range(0, M):
        n1, n2 = map(int, input().strip().split())
        if n1 not in graph.keys():
            graph[n1] = set()
        if n2 not in graph.keys():
            graph[n2] = set()
        graph[n1].add(n2)
        graph[n2].add(n1)

    dfs(N, M, V, graph)
    bfs(N, M, V, graph)
