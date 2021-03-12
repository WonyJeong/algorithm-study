import heapq
import sys


def dijkstra(edges, start):
    heap = []
    heapq.heappush(heap, (0, start))
    dp = [INF for _ in range(N+1)]
    dp[start] = 0
    while heap:
        sw, s = heapq.heappop(heap)
        if sw <= dp[s]:
            for nw, n in edges[s]:
                weight = nw + sw
                if dp[n] > weight:
                    dp[n] = weight
                    heapq.heappush(heap, (weight, n))
    return dp[1:]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, X = map(int, input().strip().split())
    edges = [[] for _ in range(N+1)]
    edges2 = [[] for _ in range(N+1)]

    for _ in range(M):
        start, end, weight = map(int, input().strip().split())
        edges[start].append((weight, end))
        edges2[end].append((weight, start))

    INF = sys.maxsize

    print(max([a+b for a, b in zip(dijkstra(edges, X), dijkstra(edges2, X))]))
