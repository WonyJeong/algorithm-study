#1206
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



def DFS(graph, V):
    visited = {}
    stack = list()
    stack.append(V)

    while stack : 
        node = stack.pop() #맨 마지막에 있는 요소 가져옴
        if node not in visited:
            visited[node] = True
            stack.extend(reversed(graph[node]))
    return visited



if __name__ == '__main__':

    N, M, V = map(int, input().strip().split())
    '''
    N : 정점의 개수
    M : 간선의 개수
    V : 탐색을 시작할 정점
    *** 조건 : 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문한다 
            => graph 각 노드(key)에 대한 간선으로 연결된 정점리스트(value)를 정렬시킨다.
            => BFS : queue이니까 그대로
            => DFS : stack이므로 나중에 들어간게 먼저 pop되므로 나중에 들어간게 정점번호가 작아야되니까
                    stack에 추가할 때 graph list reversed시켜서 넣으면 (아래)4,3,2,1(위)이렇게 들어가서
                    정점 번호 작은게 먼저 방문됨
    '''
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

    for node in DFS(graph,V):
        print(node, end=' ')
    print()
    for node in BFS(graph,V):
        print(node, end=' ')