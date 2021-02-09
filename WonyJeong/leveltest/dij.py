import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, K, graph):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, K))
    dist = [INF for _ in range(0, V + 1)]
    dist[K] = 0

    while q:
        d, v = heapq.heappop(q)
        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = w + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    return dist


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(V + 1)]
    for i in range(0, len(E)):
        u, v, w = E[i]
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = dijkstra(N, 1, graph)

    for i in range(0, len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer


if __name__ == "__main__":
