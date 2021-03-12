import heapq
import sys


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    count = 0
    while heap:
        sw, s = heapq.heappop(heap)
        if (s != end and sw <= dp[s]) or not count:
            for nw, n in edges[s]:
                weight = nw + sw
                if dp[n] > weight:
                    dp[n] = weight
                    heapq.heappush(heap, (weight, n))
        count += 1


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        start, end, weight = map(int, input().strip().split())
        edges[start].append((weight, end))

    INF = sys.maxsize

    result = INF
    for i in range(N):
        dp = [INF for _ in range(N+1)]
        dijkstra(i, i)
        result = min(result, dp[i])

    if result == INF:
        print(-1)
    else:
        print(result)
