import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, K, end, graph):
    INF = sys.maxsize
    q = []
    heapq.heappush(q, (0, K))
    dist = [INF for _ in range(0, V + 1)]
    dist[K] = 0

    while q:
        d, v = heapq.heappop(q)
        if dist[v] >= d:
            for node, w in graph[v]:
                newPath = w + d
                if dist[node] > newPath:
                    dist[node] = newPath
                    heapq.heappush(q, (newPath, node))

    return dist[end]


def solution(n, s, a, b, fares):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    sToa = 0
    sTob = 0
    aTob = dijkstra(n, a, b, graph)
    bToa = dijkstra(n, b, a, graph)
    sToAthers = []

    for i in range(1, n + 1):
        if i == s:
            continue
        elif i == a:
            sToa = dijkstra(n, s, a, graph)
        elif i == b:
            sTob = dijkstra(n, s, b, graph)
        else:
            sToAthers.append([s, i, dijkstra(n, s, i, graph)])

    answer.append(sToa + sTob)
    answer.append(sToa + aTob)
    answer.append(sTob + bToa)

    for sToAther in sToAthers:
        s, mid, price = sToAther
        price += dijkstra(n, mid, a, graph) + dijkstra(n, mid, b, graph)
        answer.append(price)
    return min(answer)


if __name__ == "__main__":
    print(
        solution(
            6,
            4,
            6,
            2,
            [
                [4, 1, 10],
                [3, 5, 24],
                [5, 6, 2],
                [3, 1, 41],
                [5, 1, 24],
                [4, 6, 50],
                [2, 4, 66],
                [2, 3, 22],
                [1, 6, 25],
            ],
        )
    )
