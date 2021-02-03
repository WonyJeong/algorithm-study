import sys

input = sys.stdin.readline

from collections import deque

## 틀림


def isBipartiteGraph(V, E, graph):
    color = [0 for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    keys = list(graph.keys())
    flag = True
    for i in range(0, len(keys)):
        if flag == False:
            print("NO")
            return
        node = keys[i]

        if visited[node] == False:
            visited[node] = True
            injectNodes = list(graph[node])

            nodeColor = 1 if color[node] == 0 else color[node]
            color[node] = nodeColor

            for injectNode in injectNodes:
                if node != injectNodes:
                    injectNodeColor = color[injectNode]
                    if injectNodeColor == 0:
                        color[injectNode] = nodeColor * -1
                    elif injectNodeColor == nodeColor:
                        color[injectNode] = nodeColor * -1
                        flag = False

    print("YES")


if __name__ == "__main__":
    K = int(input().strip())
    for _ in range(0, K):
        graph = {}
        V, E = map(int, input().strip().split())
        for _ in range(0, E):
            n1, n2 = map(int, input().strip().split())
            if n1 not in graph.keys():
                graph[n1] = set()
            if n2 not in graph.keys():
                graph[n2] = set()
            graph[n1].add(n2)
            graph[n2].add(n1)
        isBipartiteGraph(V, E, graph)
