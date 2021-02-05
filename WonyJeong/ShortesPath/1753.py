import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, E, K, graph):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, K))
    dist = [INF for _ in range(0, V + 1)]
    dist[K] = 0

    while q:
        d, v = heapq.heappop(q)
        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = dist[v] + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    for i in range(1, V + 1):
        print("INF" if dist[i] == INF else dist[i])


if __name__ == "__main__":
    V, E = map(int, input().strip().split())
    K = int(input().strip())
    graph = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))

    dijkstra(V, E, K, graph)