#1504 양방향, 주어진 두 정점 반드시 거침(각 두 정점에서 다익스트라 실행)
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def Dijkstra(graph, startNode, endNode):
    dp = [INF]*(N+1)
    dp[startNode] = 0 
    heap = []
    heapq.heappush(heap, (0, startNode))
    while len(heap) > 0 :
        weight, vertice = heapq.heappop(heap)
        if dp[vertice] < weight :
            continue
        
        for newWeight, nextNode in graph[vertice]:
            nextWeight = newWeight + weight
            if nextWeight < dp[nextNode] :
                dp[nextNode] = nextWeight
                heapq.heappush(heap, (nextWeight, nextNode))

    return dp[endNode]

if __name__ == '__main__':
    N, E = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, distance = map(int, input().strip().split())
        graph[a].append((distance, b))
        graph[b].append((distance, a))
    
    mustPassVertice1, mustPassVertice2 = map(int, input().strip().split())

    path1 = Dijkstra(graph, 1, mustPassVertice1) + Dijkstra(graph, mustPassVertice1, mustPassVertice2) + Dijkstra(graph, mustPassVertice2, N)
    path2 = Dijkstra(graph, 1, mustPassVertice2) + Dijkstra(graph, mustPassVertice2, mustPassVertice1) + Dijkstra(graph, mustPassVertice1, N)
    min_path = min(path1, path2)

    if path1 >= INF and path2 >= INF:
        print(-1)
    else:
        print(min_path)
