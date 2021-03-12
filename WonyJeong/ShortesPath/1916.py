import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, E, graph, start, end):
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
    print(dist[end])


if __name__ == "__main__":
    V = int(input().strip())
    E = int(input().strip())
    graph = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
    start, end = map(int, input().strip().split())
    dijkstra(V, E, graph, start, end)
