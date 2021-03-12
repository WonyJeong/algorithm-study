import sys


def quadtree(n, x, y):
    global graph
    result = ""
    point = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if point != graph[i][j]:
                result += "("
                result += quadtree(n//2, x, y)
                result += quadtree(n//2, x, y+n//2)
                result += quadtree(n//2, x+n//2, y)
                result += quadtree(n//2, x+n//2, y+n//2)
                result += ")"
                return result
    return point


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [input().strip() for _ in range(n)]
    print(quadtree(n, 0, 0))
