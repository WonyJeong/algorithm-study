from collections import deque
import sys

input = sys.stdin.readline


def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    graph = [[0] * (lenb+1) for _ in range(lena+1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                graph[i+1][j+1] = graph[i][j] + 1
            else:
                graph[i+1][j+1] = max(graph[i+1][j], graph[i][j+1])
    return graph


if __name__ == "__main__":

    a = input().strip()
    b = input().strip()

    print(lcs(a, b)[-1][-1])
