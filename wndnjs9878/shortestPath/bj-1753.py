#1753
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def Dijkstra(startNode,V):
    dp[startNode] = 0
    heapq.heappush(heap, (0, startNode))
    while len(heap) > 0 :
        weight, vertice = heapq.heappop(heap)
        #현재 테이블과 비교하여 더 가중치가 큰 튜플이면 무시
        if dp[vertice] < weight :
            continue
        for newWeight, nextNode in graph[vertice]:
            nextWeight = newWeight + weight
            if nextWeight < dp[nextNode]:
                dp[nextNode] = nextWeight
                heapq.heappush(heap, (nextWeight, nextNode))

    for i in range(1, V+1):
        if dp[i] == INF:
            print('INF') 
        else :
            print(dp[i])


if __name__ == '__main__':
    V, E = map(int, input().strip().split())
    startNode = int(input().strip())
    dp = [INF]*(V+1)
    heap = []
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        u, v, w = map(int, input().strip().split())
        graph[u].append((w,v))

    Dijkstra(startNode,V)