import sys

input = sys.stdin.readline


def solution(N, M, K, a, b):
    answer = [[0 for _ in range(K)] for _ in range(N)]

    for i in range(N):
        for j in range(K):
            temp = 0
            for k in range(M):
                temp += a[i][k] * b[k][j]
            answer[i][j] = temp

    for row in answer:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    a = []
    b = []
    for _ in range(N):
        a.append(list(map(int, input().strip().split())))
    M, K = map(int, input().strip().split())
    for _ in range(M):
        b.append(list(map(int, input().strip().split())))
    solution(N, M, K, a, b)
