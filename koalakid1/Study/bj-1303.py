import sys
from collections import deque


def BFS(graph, team):
    visited = [[False for _ in range(N)] for _ in range(M)]
    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]
    queue = deque()
    result = []
    for i in range(M):
        for j in range(N):
            if visited[i][j] == False and graph[i][j] == team:
                visited[i][j] = True
                queue.append((i, j))
                count = 0
                while queue:
                    x, y = queue.popleft()
                    count += 1
                    for k in range(4):
                        a = x + xm[k]
                        b = y + ym[k]
                        if 0 <= a < M and 0 <= b < N and graph[a][b] == team and visited[a][b] == False:
                            visited[a][b] = True
                            queue.append((a, b))
                result.append(count)
    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    graph = [input().strip() for _ in range(M)]
    w_list = BFS(graph, "W")
    b_list = BFS(graph, "B")

    w_sum = 0
    b_sum = 0
    for i in w_list:
        w_sum += i ** 2
    for i in b_list:
        b_sum += i ** 2
    print(w_sum, b_sum)
