import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, E, graph, start):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF for _ in range(0, V + 1)]
    while q:
        d, v = heapq.heappop(q)
        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = w + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    return dist[start]


def solution(V, E, graph):
    answer = []
    for i in range(1, V + 1):
        answer.append(dijkstra(V, E, graph, i))

    print(min(answer) if min(answer) != sys.maxsize else -1)


if __name__ == "__main__":
    V, E = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
    solution(V, E, graph)
