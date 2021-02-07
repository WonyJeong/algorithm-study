import sys

input = sys.stdin.readline


def canGo(graph):
    global R
    global C
    xm = [1, -1, 0, 0]
    ym = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if graph[i][j] == ".":
                count = 0
                for k in range(4):
                    x = i + xm[k]
                    y = j + ym[k]
                    if 0 <= x < R and 0 <= y < C and graph[x][y] == ".":
                        count += 1
                if count <= 1:
                    print(1)
                    return
    print(0)


if __name__ == "__main__":
    R, C = map(int, input().strip().split())
    graph = [input().strip() for _ in range(R)]
    canGo(graph)
