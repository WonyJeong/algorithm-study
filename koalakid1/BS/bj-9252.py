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


def lcsString(graph, a):
    result = ""
    now = graph[-1][-1]
    lena = len(graph) - 1
    lenb = len(graph[0]) - 1
    while now:
        if now - 1 == graph[lena][lenb-1] == graph[lena-1][lenb]:
            result = a[lena-1] + result
            now -= 1
            lena -= 1
            lenb -= 1
        else:
            if graph[lena][lenb-1] > graph[lena-1][lenb]:
                lenb -= 1
            else:
                lena -= 1
    return result


if __name__ == "__main__":

    a = input().strip()
    b = input().strip()

    graph = lcs(a, b)
    print(graph[-1][-1])
    print(lcsString(graph, a))
