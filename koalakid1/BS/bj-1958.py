from collections import deque
import sys

input = sys.stdin.readline


def lcs(a, b, c):
    lena = len(a)
    lenb = len(b)
    lenc = len(c)
    graph = [[[0] * (lenc+1) for _ in range(lenb + 1)] for _ in range(lena+1)]
    for i in range(lena):
        for j in range(lenb):
            for k in range(lenc):
                if a[i] == b[j] == c[k]:
                    graph[i+1][j+1][k+1] = graph[i][j][k] + 1
                else:
                    graph[i+1][j+1][k+1] = max(graph[i+1][j+1]
                                               [k], graph[i][j+1][k+1], graph[i+1][j][k+1])
    print(graph)

    return graph


if __name__ == "__main__":

    a = input().strip()
    b = input().strip()
    c = input().strip()

    print(lcs(a, b, c)[-1][-1][-1])
