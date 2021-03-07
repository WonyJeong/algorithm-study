import sys

input = sys.stdin.readline

# 이분매칭
# 이분그래프에서, left node 와 right node 를 1:1 매칭시키는 알고리즘
# maxflow.py 에서 networkflow algorithm을 구현해서, bfs를 이용한 에드먼 호프 알고리즘 적용해봤는데
# 위 문제는 bfs를 이용한 알고리즘이 아닌 dfs 를 이용해 O(VE) 시간복잡도 이내에 끝내야함
# 아래 주석으로 network flow를 이용한 알고리즘 구현해 보았는데 시간초과


def dfs(n, flow):
    if visited[n]:
        return 0

    visited[n] = True
    for i in flow[n]:
        if not left[i] or dfs(left[i], flow):
            # print(i, " -> ", n)
            # i번 째 사람을 n번째 일에 매칭
            left[i] = n
            return 1


def solution(flow):
    global left, visited
    answer = 0
    # 초기 왼쪽 노드는 연결되어 있지 않음
    left = [0 for _ in range(1001)]

    for i in range(1, N + 1):
        visited = [False for _ in range(1001)]
        if dfs(i, flow):
            answer += 1
    print(answer)


if __name__ == "__main__":
    N, M = map(int, input().split())
    flow = [[]]
    for i in range(N):
        flow.append(list(map(int, input().strip().split()))[1:])

    solution(flow)


# import sys
# from collections import deque

# input = sys.stdin.readline


# def make_flow(prv):
#     start = 0
#     end = 2001
#     flow = float("inf")

#     current = end
#     while current != start:
#         flow = min(flow, c[prv[current]][current] - f[prv[current]][current])
#         # A->Z 경로에서 가장 작은 용량 선택.
#         current = prv[current]
#     current = end

#     while current != start:
#         f[prv[current]][current] += flow
#         f[current][prv[current]] -= flow
#         current = prv[current]
#     return flow


# def bfs():
#     start = 0  # A
#     end = 2001  # Z
#     visited = [-1 for _ in range(2002)]
#     q = [start]
#     for current in q:
#         for next_ in adj[current]:
#             if c[current][next_] > f[current][next_] and visited[next_] < 0:
#                 q.append(next_)
#                 visited[next_] = current
#                 if next_ == end:
#                     return make_flow(visited)
#     return -1


# def solution():
#     answer = 0
#     while True:
#         flow = bfs()
#         if flow > 0:
#             answer += flow
#         else:
#             break
#     print(answer)


# if __name__ == "__main__":
#     global N, f, c, adj
#     N, M = map(int, input().strip().split())
#     f = [[0 for _ in range(2002)] for _ in range(2002)]  # 유량
#     c = [[0 for _ in range(2002)] for _ in range(2002)]  # 용량
#     adj = [set() for _ in range(2002)]  # 간선
#     end = 2001
#     for i in range(1, N + 1):
#         j = i + 1000
#         adj[j].add(end)
#         adj[end].add(j)
#         c[j][end] += 1
#         c[end][j] += 1

#     for u in range(M + 1):
#         if u == 0:
#             for v in range(1, N + 1):
#                 adj[u].add(v)
#                 adj[v].add(u)
#                 c[u][v] += 1
#                 c[v][u] += 1
#         else:
#             workList = list(map(int, input().strip().split()))
#             for v in workList[1:]:
#                 v_ = v + 1000
#                 adj[u].add(v_)
#                 adj[v_].add(u)
#                 c[u][v_] += 1
#                 c[v_][u] += 1
#     solution()
