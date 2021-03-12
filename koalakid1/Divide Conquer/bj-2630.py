import sys


def quadtree(n, x, y):
    global graph, blue, white
    point = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if point != graph[i][j]:
                quadtree(n//2, x, y)
                quadtree(n//2, x, y+n//2)
                quadtree(n//2, x+n//2, y)
                quadtree(n//2, x+n//2, y+n//2)
                return
    if point:
        blue += 1
        return
    else:
        white += 1
        return


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]
    blue, white = 0, 0
    quadtree(n, 0, 0)
    print(white)
    print(blue)
