import heapq
import sys


def dijkstra(x, y):
    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]
    dp[x][y] = 0
    heapq.heappush(heap, (0, x, y))
    while heap:
        now_weight, now_x, now_y = heapq.heappop(heap)
        if now_weight <= dp[now_x][now_y] and now_x != N-1 or now_y != M-1:
            for i in range(4):
                next_x = now_x + xm[i]
                next_y = now_y + ym[i]
                if 0 <= next_x < N and 0 <= next_y < M:
                    next_weight = now_weight + graph[next_x][next_y]
                    if dp[next_x][next_y] > next_weight:
                        dp[next_x][next_y] = next_weight
                        heapq.heappush(heap, (next_weight, next_x, next_y))


if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int, input().strip().split())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    INF = sys.maxsize
    dp = [[INF for _ in range(M)] for _ in range(N)]
    heap = []
    dijkstra(0, 0)
    print(dp[N-1][M-1])
