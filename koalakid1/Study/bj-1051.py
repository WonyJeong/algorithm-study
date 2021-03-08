import sys


def square(graph):
    if N == 1 or M == 1:
        print(1)
        return
    Min = min(M, N)
    result = 1
    for j in range(M-1):
        for i in range(N-1):
            for k in range(1, Min):
                if i+k >= N or j + k >= M:
                    break
                else:
                    if graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                        result = max(result, k+1)
    print(result**2)


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys
    N, M = map(int, input().strip().split())
    graph = [input().strip() for _ in range(N)]
    square(graph)

    