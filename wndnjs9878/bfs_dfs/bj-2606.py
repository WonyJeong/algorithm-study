#2606
import sys
from collections import deque
input = sys.stdin.readline


def BFS(graph, start_node):
    visited = {}
    queue = deque([])
    queue.append(start_node)

    while len(queue) > 0:
        node = queue.popleft() 
        if node not in visited:
            visited[node] = True
            for next_node in graph[node]:
                queue.append(next_node)
    return visited


if __name__ == '__main__':

    N = int(input().strip())
    M = int(input().strip())
    # 그래프 만들자 (트리구조)
    graph = {} 
    for i in range(N+1):
        graph.setdefault(i, [])

    for _ in range(M):
        vertice1, vertice2 = map(int, input().strip().split())
        graph[vertice1] += [vertice2]
        graph[vertice2] += [vertice1]
    
    for key in graph.keys() :
        graph[key].sort()

    print(len(BFS(graph,1).keys())-1)