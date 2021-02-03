import sys


def CCW(A, B, C):
    temp = 0
    temp += A[0]*B[1]+B[0]*C[1]+C[0]*A[1]
    temp -= A[1]*B[0]+B[1]*C[0]+C[1]*A[0]
    return temp


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().strip().split())))
    A = graph[0]
    result = 0
    for i in range(1, N-1):
        B = graph[i]
        C = graph[i+1]
        result += CCW(A, B, C)
    print(abs(round(result/2, 1)))
