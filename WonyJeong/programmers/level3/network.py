import sys

input = sys.stdin.readline


def dfs(node):
    stack = [node]
    while stack:
        cur = stack.pop()
        if visited[cur] == False:
            visited[cur] = True
            for inject in graph[cur]:
                if visited[inject] == False:
                    stack.append(inject)


def solution(n, computers):
    global visited, graph
    answer = 0
    visited = [False for _ in range(n)]

    graph = {}
    for i in range(0, n):
        for j in range(i, n):
            if computers[i][j] == 1:
                if i not in graph.keys():
                    graph[i] = set()
                if j not in graph.keys():
                    graph[j] = set()
                graph[i].add(j)
                graph[j].add(i)

    for node in graph.keys():
        if visited[node] == False:
            dfs(node)
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
