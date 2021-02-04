import heapq
import sys


def dijkstra(start, end):
    heapq.heappush(heap, (0, start))
    while heap:
        sw, s = heapq.heappop(heap)
        if s != end and sw <= dp[s]:
            for nw, n in edges[s]:
                weight = nw + sw
                if dp[n] > weight:
                    dp[n] = weight
                    heapq.heappush(heap, (weight, n))


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        start, end, weight = map(int, input().strip().split())
        edges[start].append((weight, end))

    INF = sys.maxsize
    dp = [INF for i in range(N+1)]
    heap = []
    start, end = map(int, input().strip().split())
    dijkstra(start, end)
    print(dp[end])
