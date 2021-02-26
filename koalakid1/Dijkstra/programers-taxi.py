import heapq
import sys

def dijkstra(K,end,n,edges):
    INF = sys.maxsize
    dp = [INF for _ in range(n+1)]
    dp[K] = 0
    heap = []
    heapq.heappush(heap, (0, K))
    while heap:
        uw, u = heapq.heappop(heap)
        if dp[u] >= uw:
            for v, w in edges[u]:
                next = w + uw
                if dp[v] > next:
                    dp[v] = next
                    heapq.heappush(heap, (next, v))
    return dp[end]
                    
def solution(n, s, a, b, fares):
    answer = 0
    edges = [[] for _ in range(n+1)]
    for u, v, w in fares:
        edges[u].append((v,w))
        edges[v].append((u,w))
    INF = sys.maxsize
    for i in range(1, n+1):
        INF = min(INF,dijkstra(s,i,n,edges) + dijkstra(i,a,n,edges) + dijkstra(i,b,n,edges))
    return INF