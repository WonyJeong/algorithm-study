#1753
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def Dijkstra(startNode,V):
    dp = [INF]*(V+1)
    heap = []
    dp[startNode] = 0 #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    heapq.heappush(heap, (0, startNode))
    while len(heap) > 0 :
        weight, vertice = heapq.heappop(heap)
        #현재 테이블과 비교하여 더 가중치가 큰 튜플이면 무시
        if dp[vertice] < weight :
            continue
        for newWeight, nextNode in graph[vertice]:
            nextWeight = newWeight + weight
            # 다음 노드까지의 가중치가 현재 다음노드가 가중치 테이블에 가지고 있는 가중치보다 작으면 조건 성립
            # 계산한 다음 노드까지의 가중치를 가중치테이블에 업데이트 하고, 최소 힙에 삽입
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
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        u, v, w = map(int, input().strip().split())
        graph[u].append((w,v))

    Dijkstra(startNode,V)