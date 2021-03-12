import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, E, graph, start, X):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF for _ in range(0, V + 1)]
    dist[start] = 0
    while q:
        d, v = heapq.heappop(q)
        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = w + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    return dist[X]


def solution(V, E, graph, X):
    answer = []
    for i in range(1, V + 1):
        answer.append(dijkstra(V, E, graph, i, X) + dijkstra(V, E, graph, X, i))

    print(max(answer))


if __name__ == "__main__":
    V, E, X = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
    solution(V, E, graph, X)
