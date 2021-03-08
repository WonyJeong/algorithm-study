import sys
from collections import deque

input = sys.stdin.readline


def make_flow(prv):
    start = 0
    end = 25
    flow = float("inf")

    current = end
    while current != start:
        flow = min(flow, c[prv[current]][current] - f[prv[current]][current])
        # A->Z 경로에서 가장 작은 용량 선택.
        current = prv[current]
    current = end

    while current != start:
        f[prv[current]][current] += flow
        f[current][prv[current]] -= flow
        current = prv[current]
    return flow


def bfs():
    start = 0  # A
    end = 25  # Z
    visited = [-1 for _ in range(52)]
    q = [start]
    for current in q:
        for next_ in adj[current]:
            if c[current][next_] > f[current][next_] and visited[next_] < 0:
                q.append(next_)
                visited[next_] = current
                if next_ == end:
                    return make_flow(visited)
    return -1


def solution():
    answer = 0
    while True:
        flow = bfs()
        if flow > 0:
            answer += flow
        else:
            break
    print(answer)


if __name__ == "__main__":
    global N, f, c, adj
    N = int(input().strip())
    f = [[0 for _ in range(52)] for _ in range(52)]  # 유량
    c = [[0 for _ in range(52)] for _ in range(52)]  # 용량
    adj = [set() for _ in range(52)]  # 간선

    for _ in range(N):
        a, b, c_ = map(str, input().strip().split())
        a = ord(a) - ord("A") if a <= "Z" else ord(a) - ord("a") + 26
        b = ord(b) - ord("A") if b <= "Z" else ord(b) - ord("a") + 26
        c_ = int(c_)
        c[a][b] += c_
        c[b][a] += c_

        adj[a].add(b)
        adj[b].add(a)
    solution() 