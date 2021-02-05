import heapq
import sys


def dijkstra(K):
    dp[K] = 0
    heapq.heappush(heap, (0, K))
    while heap:
        uw, u = heapq.heappop(heap)
        if dp[u] >= uw:
            for v, w in edges[u]:
                next = w + uw
                if dp[v] > next:
                    dp[v] = next
                    heapq.heappush(heap, (next, v))


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    V, E = map(int, input().strip().split())
    K = int(input())
    dp = [INF for _ in range(V+1)]
    heap = []

    edges = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        edges[u].append((v, w))

    dijkstra(K)
    for i in range(1, V+1):
        result = dp[i]
        if result == INF:
            print("INF")
        else:
            print(result)
