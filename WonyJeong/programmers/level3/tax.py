import sys
import heapq

input = sys.stdin.readline

# q : w, v, count
def specialShortestPath(V, E, x, y, graph):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, x))

    dist = [INF for _ in range(0, V + 1)]
    dist[x] = 0

    while q:
        d, v = heapq.heappop(q)

        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = w + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    return -1 if dist[y] == INF else dist[y]


if __name__ == "__main__":
    V, E = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    x, y = map(int, input().strip().split())
    # specialShortestPath(V, E, x, y, graph)

    path = [1, x, y, V]
    answer = []
    for _ in range(2):
        sum = 0
        for i in range(0, 3):
            temp = specialShortestPath(V, E, path[i], path[i + 1], graph)
            if temp == -1:
                sum = sys.maxsize
                break
            sum += temp
        path = [1, y, x, V]
        answer.append(sum)

    print(-1 if min(answer) == sys.maxsize else min(answer))
