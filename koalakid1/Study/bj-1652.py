import sys


def Checking(graph, axis):
    count = 0
    for i in range(N):
        checker = 0
        for j in range(N):
            if axis == 0:
                start = graph[i][j]
            else:
                start = graph[j][i]
            if start == ".":
                checker += 1
            else:
                if checker >= 2:
                    count += 1
                checker = 0
        if checker >= 2:
            count += 1
    return count


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    graph = [input().strip() for _ in range(N)]
    w = Checking(graph, 0)
    h = Checking(graph, 1)
    print(w, h)
